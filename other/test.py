# >>> sorted(student_objects, key=lambda student: student.age)   # sort by age

import numpy as np
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.graph_objs as go


number = 100
number +=1


A = np.zeros((number**2,3))

for idx, row in enumerate(A):
	row[0] = int(idx % number)
	row[1] = int((idx/number))
	row[2] = int(row[0]*row[1])

trace = go.Heatmap(z=A[:,2], y=A[:,1], x=A[:,0])
data=[trace]
print data
plot(data, filename='basic-heatmap')



