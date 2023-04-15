import dash
import dash_html_components as html

# create instantiation of app
app = dash.Dash(__name__)

# layout
app.layout = html.Div([html.H1('Hello, World!')])

# run
if __name__ == '__main__':
    app.run_server(debug=True)

'''%config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt

from plotly.tools import mpl_to_plotly

mpl_fig, ax = plt.subplots()

ax.scatter(x=[1, 2, 3], y=[23, 12, 34])

plotly_fig = mpl_to_plotly(mpl_fig)

plotly_fig'''
