from flask import Flask,render_template, request



app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def show_Location():
    if request.method == "POST":
        location = request.form['location']
        station, wheelchair_accessible = find_stop_near(location)
        return render_template('OutPage.html', location=station, wheelchair_accessible=wheelchair_accessible)
    else:
        return render_template('FirstPage.html')


if __name__ == '__main__':
    app.run(debug=True)