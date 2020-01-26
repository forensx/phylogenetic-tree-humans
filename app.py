import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

evolution = pd.read_csv("Evolution.csv")

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

nodes = [
    {
        'data': {'id': commonName, 'label': label, 'mode': mode, 'cranialCapacity': cranialCapacity, 'origin': origin, 'dead': dead, 'habitat': habitat, 'geography': geography, 'fossil': fossil},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for commonName, label, mode, cranialCapacity, origin, dead, habitat, geography, fossil, lat, long in (
        ('human', evolution['Genus'][0] + " " + evolution['Species'][0], evolution['Movement'][0], evolution['Cranial Capacity'][0], evolution['Origin'][0], evolution['Dead'][0], evolution['Habitat'][0], evolution['Geographical Origin'][0], evolution['Fossils'][0], 34.03, -118.25 ),
        ('neand', evolution['Genus'][1] + " "  + evolution['Species'][1], evolution['Movement'][1], evolution['Cranial Capacity'][1], evolution['Origin'][1],evolution['Dead'][1], evolution['Habitat'][1], evolution['Geographical Origin'][1], evolution['Fossils'][1],  40.71, -74 ),
        ('erect', evolution['Genus'][2] + " "  + evolution['Species'][2], evolution['Movement'][2], evolution['Cranial Capacity'][2], evolution['Origin'][2],evolution['Dead'][2], evolution['Habitat'][2], evolution['Geographical Origin'][2], evolution['Fossils'][2], 43.65, -79.38 ),
        ('habillis', evolution['Genus'][3] + " "  + evolution['Species'][3], evolution['Movement'][3], evolution['Cranial Capacity'][3], evolution['Origin'][3],evolution['Dead'][3], evolution['Habitat'][3], evolution['Geographical Origin'][3], evolution['Fossils'][3], 45.50, -73.57 ),
        ('afarensis', evolution['Genus'][4] + " "  + evolution['Species'][4], evolution['Movement'][4], evolution['Cranial Capacity'][4], evolution['Origin'][4], evolution['Dead'][4],evolution['Habitat'][4], evolution['Geographical Origin'][4], evolution['Fossils'][4], 49.28, -123.12 ),
        ('pan', evolution['Genus'][5] + " "  + evolution['Species'][5], evolution['Movement'][5], evolution['Cranial Capacity'][5], evolution['Origin'][5], evolution['Dead'][5],evolution['Habitat'][5], evolution['Geographical Origin'][5], evolution['Fossils'][5], 41.88, -87.63 ),
        ('gorilla', evolution['Genus'][6] + " "  + evolution['Species'][6], evolution['Movement'][6], evolution['Cranial Capacity'][6], evolution['Origin'][6],evolution['Dead'][6], evolution['Habitat'][6], evolution['Geographical Origin'][6], evolution['Fossils'][6], 42.36, -71.06 )
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('human', 'neand'),
        ('neand', 'chi'),
        ('hou', 'erect'),
        ('erect', 'habillis'),
        ('habillis', 'afarensis'),
        ('afarensis', 'pan'),
        ('gorilla', 'human'),

    )
]



default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'label': 'data(label)'
        }
    }
]


app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-event-callbacks-1',
        layout={'name': 'preset'},
        elements=edges+nodes,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    ),
    html.Pre(id='cytoscape-tapNodeData-json', style=styles['pre'])
])


@app.callback(Output('cytoscape-tapNodeData-json', 'children'),
              [Input('cytoscape-event-callbacks-1', 'tapNodeData')])
def displayTapNodeData(data):
    return json.dumps(data, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)