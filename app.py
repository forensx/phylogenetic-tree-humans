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
    'edges-color': '#689775',
    'node-color': '#C7493A',
    'header-color': '#A33327',
    'sidebar-text-color': '#FFFFFF'
}


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Human Origins: Phylogeny"
app.css.config.serve_locally = False


evolution = pd.read_csv("Evolution.csv")

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

nodes = [
    {
        'data': {'id': commonName, 'label': label, 'mode': mode, 'justification': justification, 'cranialCapacity': cranialCapacity, 'origin': origin, 'dead': dead, 'habitat': habitat, 'geography': geography, 'fossil': fossil},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for commonName, label, mode, justification, cranialCapacity, origin, dead, habitat, geography, fossil, lat, long in (
        ('ancestor', 'Common Ancestor', '?', '?',
         '?', '?', '?', '?', '?', '?', 3, -30),
        ('human', evolution['Genus'][0] + " " + evolution['Species'][0], evolution['Movement'][0], evolution['Justification'][0], evolution['Cranial Capacity'][0], evolution['Origin']
         [0], evolution['Dead'][0], evolution['Habitat'][0], evolution['Geographical Origin'][0], evolution['Fossils'][0], 32, -4),
        ('neand', evolution['Genus'][1] + " " + evolution['Species'][1], evolution['Movement'][1], evolution['Justification'][1], evolution['Cranial Capacity'][1], evolution['Origin']
         [1], evolution['Dead'][1], evolution['Habitat'][1], evolution['Geographical Origin'][1], evolution['Fossils'][1],  34, -14),
        ('erect', evolution['Genus'][2] + " " + evolution['Species'][2], evolution['Movement'][2], evolution['Justification'][2], evolution['Cranial Capacity'][2], evolution['Origin']
         [2], evolution['Dead'][2], evolution['Habitat'][2], evolution['Geographical Origin'][2], evolution['Fossils'][2], 26, -20),
        ('habillis', evolution['Genus'][3] + " " + evolution['Species'][3], evolution['Movement'][3], evolution['Justification'][3], evolution['Cranial Capacity'][3], evolution['Origin']
         [3], evolution['Dead'][3], evolution['Habitat'][3], evolution['Geographical Origin'][3], evolution['Fossils'][3], 21, -23),
        ('afarensis', evolution['Genus'][4] + " " + evolution['Species'][4], evolution['Movement'][4], evolution['Justification'][4], evolution['Cranial Capacity'][4], evolution['Origin']
         [4], evolution['Dead'][4], evolution['Habitat'][4], evolution['Geographical Origin'][4], evolution['Fossils'][4], 16, -30),
        ('pan', evolution['Genus'][5] + " " + evolution['Species'][5], evolution['Movement'][5], evolution['Justification'][5], evolution['Cranial Capacity'][5], evolution['Origin']
         [5], evolution['Dead'][5], evolution['Habitat'][5], evolution['Geographical Origin'][5], evolution['Fossils'][5], 34, -41),
        ('gorilla', evolution['Genus'][6] + " " + evolution['Species'][6], evolution['Movement'][6], evolution['Justification'][6], evolution['Cranial Capacity'][6], evolution['Origin']
         [6], evolution['Dead'][6], evolution['Habitat'][6], evolution['Geographical Origin'][6], evolution['Fossils'][6], 40, -53),
        ('invis1', '', '?', '?',
         '?', '?', '?', '?', '?', '?', 15, -20),
        ('invis2', '', '?', '?',
         '?', '?', '?', '?', '?', '?', 18, -16),
        ('invis3', '', '?', '?',
         '?', '?', '?', '?', '?', '?', 26, -9),
        ('invis4', '', '?', '?',
         '?', '?', '?', '?', '?', '?', 32, -47),
        ('invis5', '', '?', '?',
         '?', '?', '?', '?', '?', '?', 8, -26)
         
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
            'background-color': color_scheme['node-color'],
            'label': 'data(label)',
            'line-color': color_scheme['edges-color']
        }
    }
]


app.layout = html.Div(children=[
    html.Div([  # START FLEX CONTAINER
        # START LEFT HALF
        html.Div([
            cyto.Cytoscape(
                id='cytoscape-event-callbacks-2',
                layout={'name': 'preset'},
                elements=edges+nodes,
                stylesheet=default_stylesheet,
                autoungrabify=True,
                autolock=True,
                maxZoom=1.5,
                minZoom=0.8,
                style={'width': '100%', 'height': '100%'}
            )
        ], style={'margin': '0px',
                  'padding': '0px',
                  'grid-area': '1 / 1 / 2 / 3',
                  'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.25)',
                  'background':'#2D2C2C'
                  }),
        # START RIGHT HALF
        html.Div([
            html.Div([
                html.Div(id='cytoscape-tapNodeGenus-output',
                         style={
                             'font-size': '2em',
                             'font-weight': 'bold',
                             'color': color_scheme['header-color']
                         }),
                html.Div(id='cytoscape-tapNodeMode-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeJustification-output',
                         style={
                             'font-size': '1em',
                             'margin-top': '4%',
                             'text-align': 'justify',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeCranial-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeOrigin-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeDead-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeHabitat-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeGeography-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         }),
                html.Div(id='cytoscape-tapNodeFossil-output',
                         style={
                             'font-size': '1.2em',
                             'margin-top': '8%',
                             'color': color_scheme['sidebar-text-color']
                         })
            ], style={
                'padding': '50px',
            })
        ], style={
            'margin': '0px',
            'padding': '0px',
            'grid-area': '1 / 3 / 2 / 4',
            'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.25)',
            'background':'#2D2C2C'
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
], style={
    # 'margin': '0px',
    # 'padding': '0px',
    # 'backgroundColor': color_scheme['background-color'], #Background set in assets/style.css
})

# 6D7E7B
# color_scheme['dark-green']


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
