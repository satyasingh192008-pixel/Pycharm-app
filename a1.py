
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

server = app.server

app.layout = dbc.Container([
    my_text := dbc.Input(
        id='my_text',
        value='Type Text new now'
    ),

    my_output := dcc.Markdown(
        id='my_output',
        children=''
    ),
])

@app.callback(
    Output(component_id='my_output', component_property='children'),
    Input(component_id='my_text', component_property='value')
)
def update_text(el_texto):
    return el_texto

if __name__ == '__main__':
    app.run(debug=True)
