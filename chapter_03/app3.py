import plotly.graph_objects as go

fig = go.Figure()
fig.add_scatter(x=[1, 2, 3], y=[4, 2, 3])
fig.layout.title = 'The Figure Title'

fig.layout.xaxis.title = 'The X-axis title'

fig.layout.yaxis.title = 'The Y-axis title'

fig.show(config={'displaylogo': False,
                 'modeBarButtonsToAdd':[
                     'drawrect',
                     'drawcircle',
                     'eraseshape'
                 ]
                 })

fig.write_html('html_plot.html',
               config={'toImageButtonOptions': {'format': 'svg'}})
