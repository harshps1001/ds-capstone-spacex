# SpaceX Launch Dashboard — Plotly Dash
# Harshpreet Singh | IBM Applied Data Science Capstone

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/spacex_launch_dash.csv")
max_payload = df["Payload Mass (kg)"].max()
min_payload = df["Payload Mass (kg)"].min()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "fontSize": 40}),

    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in df["Launch_Site"].unique()],
        value="ALL",
        placeholder="Select a Launch Site",
        searchable=True
    ),

    html.Br(),
    html.Div(dcc.Graph(id="success-pie-chart")),
    html.Br(),

    html.P("Payload range (kg):"),
    dcc.RangeSlider(
        id="payload-slider",
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload]
    ),

    html.Div(dcc.Graph(id="success-payload-scatter-chart")),
])

@app.callback(Output("success-pie-chart", "figure"),
              Input("site-dropdown", "value"))
def update_pie(selected_site):
    if selected_site == "ALL":
        fig = px.pie(df, values="Class", names="Launch_Site",
                     title="Total Success Launches by Site")
    else:
        filtered = df[df["Launch_Site"] == selected_site]
        fig = px.pie(filtered, names="Class",
                     title=f"Success vs Failure for {selected_site}",
                     color_discrete_map={0: "red", 1: "green"})
    return fig

@app.callback(Output("success-payload-scatter-chart", "figure"),
              [Input("site-dropdown", "value"),
               Input("payload-slider", "value")])
def update_scatter(selected_site, payload_range):
    filtered = df[(df["Payload Mass (kg)"] >= payload_range[0]) &
                  (df["Payload Mass (kg)"] <= payload_range[1])]
    if selected_site != "ALL":
        filtered = filtered[filtered["Launch_Site"] == selected_site]
    fig = px.scatter(filtered, x="Payload Mass (kg)", y="Class",
                     color="Booster Version Category",
                     title="Payload Mass vs Landing Outcome")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
