# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Exercise 3
# Create a visualization with interactivity. Similar to Exercise 2,
# you can decide what you want to use as data and
# chart type.

# initialize Dash environment
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/cereal.csv')

# set up an layout
app.layout = html.Div(children=[

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                go.Scatter(
                # setting x as fat, and y as calories (points represent data)
                    x= df['fat'], 
                    y = df['calories'], 
                mode = 'markers',
                text = df ['name'],
                marker = {
                    'size': 12,
                    'color': 'rgb(0,255,0)'
                }
            ) 
        ],
            # configure the layout of the visualization --
            # set the title 
            'layout': {
                'title': 'Fat vs. Calories',
                'xaxis': {'title': 'Fat (g)'},
                'yaxis': {'title': 'Calories'}
            }
        }
    )
])

if __name__ == '__exercise3__':
    # start the Dash app
    app.run_server(debug=True)

