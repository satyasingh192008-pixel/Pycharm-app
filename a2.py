import os
from dash import Dash, html, Input, Output, dcc
import plotly.express as px

df = px.data.iris()

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Iris Flower Analysis Dashboard'),
    html.Label("Select Flower Species"),
    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"}
        ],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="iris_graph")
])

@app.callback(
    Output(component_id="iris_graph", component_property="figure"),
    Input(component_id="species_dropdown", component_property="value")
)

def update_graph(selected_species):

    filtered_df = df[df["species"] == selected_species]

    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title="Iris Dataset Graph"
    )

    return fig

def run_app():
    """Run the Dash dev server locally or bind to $PORT when hosted."""
    port = int(os.environ.get("PORT", 8050))
    is_render = "PORT" in os.environ
    app.run(
        host="0.0.0.0" if is_render else "127.0.0.1",
        port=port,
        debug=not is_render,
    )


if __name__ == "__main__":
    run_app()
