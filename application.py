import dash
import dash_core_components as dcc
import dash_html_components as html

import geopandas as gp
import plotly.express as px

dash_app = dash.Dash()
app = dash_app.server
Rd =gp.read_file("RotaryDistricts.geojson").to_crs("7844")

fig = px.choropleth(Rd, geojson="RotaryDistricts.geojson", color="RotaryDistrict",
                    projection="mercator"
                   )


dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Ben's silly map
    '''),

    dcc.Graph(
        id="map",
        figure=fig

    )
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)