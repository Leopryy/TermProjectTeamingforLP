from flask import Flask,render_template, request
from find import finaEVS


app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def show_Location():
    if request.method == "POST":
        Sta = request.form['Sta']
        loc = request.form['loc']
        maps, table = finaEVS(Sta,loc)
        return render_template('OutPage.html', result = maps.show())
    else:
        return render_template('FirstPage.html')


if __name__ == '__main__':
    app.run(debug=True)