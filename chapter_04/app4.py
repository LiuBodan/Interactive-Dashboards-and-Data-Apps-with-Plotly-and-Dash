import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly.express as px
import cv2

import numpy as np
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly



app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('Analysis of Iris data using scatter matrix'),
    dcc.Dropdown(
        id="dropdown",
        options=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
        value=['sepal_length', 'sepal_width'],
        multi=True
    ),
    dcc.Graph(id="graph"),
    dcc.Slider
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(dims):
    img = cv2.imread('../img/image_t_264_c_0_z_492.png')
    fig = px.imshow(img)
    return fig

if __name__ == '__main__':
    app.run_server()

'''
mpl_fig, ax = plt.subplots()

ax.scatter(x=[1, 2, 3], y=[23, 12, 34])

plotly_fig = mpl_to_plotly(mpl_fig)
'''


