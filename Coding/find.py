import pandas as pd
us_cities = pd.read_csv("Coding/v1 (3).csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "ZIP"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()