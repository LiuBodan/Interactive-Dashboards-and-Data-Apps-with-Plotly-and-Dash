import dash
import dash_core_components as dcc  # interactive
import dash_html_components as html
from dash.dependencies import Output, Input

app = dash.Dash(__name__)

# frontend
app.layout = html.Div([
    # interactive drop down menue
    dcc.Dropdown(id='color_dropdown',  # assign unique id to object
                 options=[{'label': color, 'value': color} for color in ['blue', 'green', 'yellow']]),
    #
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id='color_output') # new container
])


# backend
# callback functions are decorators, needs input, output and function
# provide output before input
@app.callback(Output('color_output', 'children'),
              Input('color_dropdown', 'value'))
def display_selected_color(color):
    if color is None:
        color = 'nothing'
    return 'You selected ' + color


if __name__ == '__main__':
    app.run_server(debug=True)
