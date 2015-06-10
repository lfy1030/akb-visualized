# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Scatter(
    x=[1, 2, 3, 4, 5],
    y=[6, 8, 7, 8, 6],
    mode='lines+markers',
    name="test",
    line=Line(
        shape='spline'
    )
)

data = Data([trace1])
layout = Layout(
    legend=Legend(
        y=0.5,
        traceorder='reversed',
        font=Font(
            size=16
        ),
        yref='paper'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='line-shapes')