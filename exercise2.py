# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.


# initialize Dash environment
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/data_car_2004.csv')

# set up an layout
app.layout = html.Div(children=[

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                go.Scatter(
                # setting x as retail cost, and y as dealers cost (points represent data)
                    x= df['Retail Price'], 
                    y = df['Dealer Cost'], 
                mode = 'markers',
                text = df ['Vehicle Name'],
                marker = {
                    'size': 12,
                    'color': 'rgb(255,0,0)'
                }
            ) 
        ],
            # configure the layout of the visualization --
            # set the title 
            'layout': {
                'title': 'Vehicles Retail Price vs. Dealer Cost',
                'xaxis': {'title': 'Retail Price'},
                'yaxis': {'title': 'Dealer Cost'}
            }
        }
    )
])

if __name__ == '__exercise2__':
    # start the Dash app
    app.run_server(debug=True)
