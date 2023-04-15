import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly

mpl_fig, ax = plt.subplots()

ax.scatter(x=[1, 2, 3], y=[23, 12, 34])

plotly_fig = mpl_to_plotly(mpl_fig)

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
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(dims):
    gapminder = px.data.gapminder()

    fig = px.scatter(data_frame=gapminder,

           x='gdpPercap',

           y='lifeExp',

           size='pop',

           facet_col='continent',

           color='continent',

           title='Life Expectancy and GDP per capita. 1952 - 2007',

           labels={'gdpPercap': 'GDP per Capita',

                   'lifeExp': 'Life Expectancy'},

           log_x=True,

           range_y=[20, 100],

           hover_name='country',

           animation_frame='year',

           height=600,

           size_max=90)
    return fig

if __name__ == '__main__':
    app.run_server()




