# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto

import json
filename = "phylo_network.json"
with open(filename, 'r') as filename:
    data = json.load(filename)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "ForensX Phylogenetic Tree"

print(data)

app.layout = html.Div(children=[
    html.Div([
        cyto.Cytoscape(
            id='human-phylogenetic-tree',
            elements=data,
            layout={'name': 'preset'},
            style = {'height': '100vh',
        'width': '100vw', 'padding': '0',
        'margin': '0'}
        )
    ], style = {
        'padding': '0',
        'margin': '0'
    })
])  # -*- coding: utf-8 -*-

if __name__ == '__main__':
    app.run_server(debug=True)
