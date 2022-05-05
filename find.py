
def finaEVS(Sta,loc):
    import pandas as pd
    us_cities = pd.read_csv("v1 (3).csv")

    df1 = us_cities[us_cities['State'].str.contains(Sta)]
    df = df1[us_cities['City'].str.contains(loc)]
    print(df)

    import plotly.express as px


    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="City", hover_data=["Station Name", "Street Address", "ZIP", "Access Days Time", "Access Code"],
                            color_discrete_sequence=["fuchsia"], zoom=10, height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig, df