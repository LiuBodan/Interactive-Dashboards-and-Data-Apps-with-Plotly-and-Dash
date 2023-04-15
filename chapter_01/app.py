import dash
import dash_html_components as html # layout
import dash_bootstrap_components as dbc # abstrct blocks for layout

# create instantiation of app
app = dash.Dash(__name__,
                external_stylesheets=
                [dbc.themes.BOOTSTRAP])

# layout
app.layout = html.Div([

    html.H1('Poverty And Equity Database',

            style={'color': 'blue',

                   'fontSize': '40px'}),

    html.H2('The World Bank'),

    html.P('Key Facts:'),
    # list elements
    html.Ul([
        # python list
        html.Li('Number of Economies: 170'),

        html.Li('Temporal Coverage: 1974 - 2019'),

        html.Li('Update Frequency: Quarterly'),

        html.Li('Last Updated: March 18, 2020'),

        html.Li([

            'Source: ',
            # link
          html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',         href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')

        ])

    ])

])

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
