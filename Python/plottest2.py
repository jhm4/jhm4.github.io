import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime
x = [
    datetime(year=2013, month=10, day=4),
    datetime(year=2013, month=11, day=5),
    datetime(year=2013, month=12, day=6)
    ]

data = [
         go.Scatter(x=x,y=[1, 3, 6])
       ]
py.iplot(data)

fig = py.get_figure("https://plot.ly/~Houston_Martinez/0/")