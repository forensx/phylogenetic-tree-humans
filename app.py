import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

color_scheme = {
    'background-color': '#161616',  # set this in assets/style.css as well
    'edge-color': '#689775',
    'node-color': '#C7493A',
    'header-color': '#C7493A',
    'sidebar-text-color': '#FFFFFF',
    'extant-color': '#3A83C7'
}


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Human Origins: Phylogeny"
app.css.config.serve_locally = False

server = app.server

evolution = pd.read_csv("Evolution.csv")

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

nodes = [
    {
        'data': {'id': commonName, 'label': label, 'mode': mode, 'justification': justification, 'cranialCapacity': cranialCapacity, 'origin': origin, 'dead': dead, 'habitat': habitat, 'geography': geography, 'fossil': fossil, 'size': size},
        'position': {'x': 15*lat, 'y': -15*long},
        'classes': classes
    }
    for commonName, label, mode, justification, cranialCapacity, origin, dead, habitat, geography, fossil, size, lat, long, classes in (
        ('ancestor', 'Common Ancestor', 'Unknown', 'Unknown', 'Unknown',
         'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 50, 3, -30, "extinct"),
        ('human', evolution['Genus'][0] + " " + evolution['Species'][0], evolution['Movement'][0], evolution['Justification'][0], evolution['Cranial Capacity'][0], evolution['Origin']
         [0], evolution['Dead'][0], evolution['Habitat'][0], evolution['Geographical Origin'][0], evolution['Fossils'][0], 50, 83, 50, "extanct"),
        ('neand', evolution['Genus'][1] + " " + evolution['Species'][1], evolution['Movement'][1], evolution['Justification'][1], evolution['Cranial Capacity'][1], evolution['Origin']
         [1], evolution['Dead'][1], evolution['Habitat'][1], evolution['Geographical Origin'][1], evolution['Fossils'][1], 50,  78, 35, "extinct"),
        ('erect', evolution['Genus'][2] + " " + evolution['Species'][2], evolution['Movement'][2], evolution['Justification'][2], evolution['Cranial Capacity'][2], evolution['Origin']
         [2], evolution['Dead'][2], evolution['Habitat'][2], evolution['Geographical Origin'][2], evolution['Fossils'][2], 50, 68, 25, "extinct"),
        ('habillis', evolution['Genus'][3] + " " + evolution['Species'][3], evolution['Movement'][3], evolution['Justification'][3], evolution['Cranial Capacity'][3], evolution['Origin']
         [3], evolution['Dead'][3], evolution['Habitat'][3], evolution['Geographical Origin'][3], evolution['Fossils'][3], 50, 58, 15, "extinct"),
        ('afarensis', evolution['Genus'][4] + " " + evolution['Species'][4], evolution['Movement'][4], evolution['Justification'][4], evolution['Cranial Capacity'][4], evolution['Origin']
         [4], evolution['Dead'][4], evolution['Habitat'][4], evolution['Geographical Origin'][4], evolution['Fossils'][4], 50, 38, -5, "extinct"),
        ('pan', evolution['Genus'][5] + " " + evolution['Species'][5], evolution['Movement'][5], evolution['Justification'][5], evolution['Cranial Capacity'][5], evolution['Origin']
         [5], evolution['Dead'][5], evolution['Habitat'][5], evolution['Geographical Origin'][5], evolution['Fossils'][5], 50, 63, -70, "extanct"),
        ('gorilla', evolution['Genus'][6] + " " + evolution['Species'][6], evolution['Movement'][6], evolution['Justification'][6], evolution['Cranial Capacity'][6], evolution['Origin']
         [6], evolution['Dead'][6], evolution['Habitat'][6], evolution['Geographical Origin'][6], evolution['Fossils'][6], 50, 63, -90, "extanct"),
        ('ardipith', evolution['Genus'][7] + " " + evolution['Species'][7], evolution['Movement'][7], evolution['Justification'][7], evolution['Cranial Capacity'][7], evolution['Origin']
         [7], evolution['Dead'][7], evolution['Habitat'][7], evolution['Geographical Origin'][7], evolution['Fossils'][7], 50, 28, -15, "extinct"),
        ('panthrop', evolution['Genus'][8] + " " + evolution['Species'][8], evolution['Movement'][8], evolution['Justification'][8], evolution['Cranial Capacity'][8], evolution['Origin']
         [8], evolution['Dead'][8], evolution['Habitat'][8], evolution['Geographical Origin'][8], evolution['Fossils'][8], 50, 48, 5, "extinct"),
        ('invisTop1', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 13, -20, "extinct"),
        ('invisTop2', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 23, -10, "extinct"),
        ('invisTop3', '', '?', '?', '?', '?',
         '?', '?', '?', '?', 1, 33, 0, "extinct"),
        ('invisTop4', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 43, 10, "extinct"),
        ('invisTop5', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 53, 20, "extinct"),
        ('invisTop6', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 63, 30, "extinct"),
        ('invisTop7', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 73, 40, "extinct"),
        ('invisBot1', '', '?', '?', '?', '?', '?',
         '?', '?', '?', 1, 38, -65, "extinct")
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('ancestor', 'invisTop1'),
        ('invisTop1', 'invisTop2'),
        ('invisTop2', 'invisTop3'),
        ('invisTop3', 'invisTop4'),
        ('invisTop4', 'invisTop5'),
        ('invisTop5', 'invisTop6'),
        ('invisTop6', 'invisTop7'),
        ('ancestor', 'invisBot1'),
        ('invisTop1', 'pan'),
        ('invisTop2', 'ardipith'),
        ('invisTop3', 'afarensis'),
        ('invisTop4', 'panthrop'),
        ('invisTop5', 'habillis'),
        ('invisTop6', 'erect'),
        ('invisTop7', 'neand'),
        ('invisTop7', 'human'),
        ('invisBot1', 'gorilla')

    )
]


default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': color_scheme['node-color'],
            'label': 'data(label)',
            'color': 'white',
            'width': 'data(size)',
            'height': 'data(size)',
            'font-size': '24',
            "text-valign": "center",
            "text-halign": "right"
        }
    },
    {
        'selector': '.extanct',
        'style': {
            'background-color': '#3A83C7'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'line-color': color_scheme['edge-color'],
            'width': '10'
        }
    }
]


app.layout = html.Div(children=[
    html.Div([  # START FLEX CONTAINER
        # START LEFT HALF
        html.Div([
            html.Div([
                html.Div([
                    'Human Origins'
                ], style={
                    'grid-area': '1 / 1 / 2 / 5',
                    'color': color_scheme['header-color'],
                    'font-size': '1.8em',
                    'font-weight': 'bold',
                    'padding-left': '10%'
                }),
                html.Div([
                    html.Div([
                    ], style={
                        'height': '25px',
                        'width': '25px',
                        'background-color': color_scheme['extant-color'],
                        'border-radius': '50%',
                        'display': 'inline-block'
                    }),
                    html.Div([
                        'Extant'
                    ], style={
                        'color': color_scheme['sidebar-text-color']
                    }),
                    html.Div([
                    ], style={
                        'height': '25px',
                        'width': '25px',
                        'background-color': color_scheme['node-color'],
                        'border-radius': '50%',
                        'display': 'inline-block'
                    }),
                    html.Div([
                        'Extinct'
                    ], style={
                        'color': color_scheme['sidebar-text-color']
                    })
                ], style={
                    'grid-area': '1 / 5 / 2 / 7',
                    'display': 'grid',
                    'grid-template-columns': '40px 100px 40px 100px',
                    'grid-template-rows': '1fr',
                    'grid-column-gap': '1px',
                    'grid-row-gap': '0px',
                    'align-items': 'center'
                })
            ],
                style={
                'box-shadow': '0px 4px 4px rgba(0, 0, 0, 0.25)',
                'grid-area': '1 / 1 / 2 / 2',
                'display': 'grid',
                'grid-template-columns': 'repeat(6, 1fr)',
                'grid-template-rows': '1fr',
                'grid-column-gap': '0px',
                'grid-row-gap': '6px',
                'align-items': 'center'
            }),
            cyto.Cytoscape(
                id='cytoscape-event-callbacks-2',
                layout={'name': 'preset'},
                elements=edges+nodes,
                stylesheet=default_stylesheet,
                autoungrabify=True,
                autolock=True,
                maxZoom=3,
                minZoom=0.38,
                zoomingEnabled=True,
                userZoomingEnabled=True,
                style={'width': '100%', 'height': '100%',
                       'grid-area': '2 / 1 / 11 / 2'}
            )
        ], style={'margin': '0px',
                  'padding': '0px',
                  'grid-area': '1 / 1 / 2 / 3',
                  'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.25)',
                  'background': '#2D2C2C',
                  'display': 'grid',
                  'grid-template-columns': '1fr',
                  'grid-template-rows': 'repeat(10, 1fr)',
                  'grid-column-gap': '0px',
                  'grid-row-gap': '1px',
                  }),
        # START RIGHT HALF
        html.Div([
            html.Div([
                html.Div(id='cytoscape-tapNodeGenus-output',
                         style={
                             'font-size': '1.7em',
                             'font-weight': 'bold',
                             'color': color_scheme['header-color']
                         }),
                html.Div(id='cytoscape-tapNodeMode-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeJustification-output',
                         style={
                             'font-size': '0.9em',
                             'margin-top': '3%',
                             'text-align': 'justify',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeCranial-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeOrigin-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeDead-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeHabitat-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeGeography-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeFossil-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '5%',
                             'color': color_scheme['sidebar-text-color']
                         })
            ], style={
                'padding': '50px',
                'overflow-wrap': 'break-word',
                'word-wrap': 'break-word',
                'hyphens': 'auto'
            })
        ], style={
            'margin': '0px',
            'padding': '0px',
            'grid-area': '1 / 3 / 2 / 4',
            'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.25)',
            'background': '#2D2C2C'
        })
    ], style={
        'display': 'grid',
        'grid-template-columns': 'repeat(3, 1fr)',
        'grid-template-rows': '1fr',
        'grid-column-gap': '35px',
        'grid-row-gap': '0px',
        'width': '90vw',
        'height': '95vh',
        'margin': 'auto',
        'padding': '0px',
        'paddingTop': '20px',
        'justify-content': 'center',

    })
])


@app.callback([Output('cytoscape-tapNodeGenus-output', 'children'),
               Output('cytoscape-tapNodeMode-output', 'children'),
               Output('cytoscape-tapNodeJustification-output', 'children'),
               Output('cytoscape-tapNodeCranial-output', 'children'),
               Output('cytoscape-tapNodeOrigin-output', 'children'),
               Output('cytoscape-tapNodeDead-output', 'children'),
               Output('cytoscape-tapNodeHabitat-output', 'children'),
               Output('cytoscape-tapNodeGeography-output', 'children'),
               Output('cytoscape-tapNodeFossil-output', 'children')],
              [Input('cytoscape-event-callbacks-2', 'tapNodeData')])
def displayTapNodeData(data):
    if data:
        genusName = data['label']
        mode = "Mode of Transportation: " + data['mode']
        justification = data['justification']
        cranial = "Cranial Capacity: " + data['cranialCapacity']
        origin = "Origin: " + data['origin'] + " years ago"
        if str(data['dead']) == "Present":
            dead = "Extinction date: N/A (still present)"
        else:
            dead = "Extinction date: " + data['dead'] + " years ago"
        habitat = "Habitat: " + data['habitat']
        geography = "Geography: " + data['geography']
        fossil = "Fossil Count: " + str(data['fossil'])
        return genusName, mode, justification, cranial, origin, dead, habitat, geography, fossil
    else:
        genusName = "Click on a node to learn more about it!"
        mode = ""
        justification = ""
        cranial = ""
        origin = ""
        dead = ""
        habitat = ""
        geography = ""
        fossil = ""
        return genusName, mode, justification, cranial, origin, dead, habitat, geography, fossil


if __name__ == '__main__':
    app.run_server(debug=True)
