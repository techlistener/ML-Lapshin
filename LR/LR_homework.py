from sklearn.cluster import KMeans
from sklearn.svm import SVC
import numpy as np
import plotly.graph_objects as go

range_min = 0
range_max = 200
points_count = 50
point_size = 5


def get_z_coordinate_by_formula(x_coord, y_coord):
    return (-svc.intercept_[0] - svc.coef_[0][0] * x_coord - svc.coef_[0][1] * y_coord) / svc.coef_[0][2]


x = np.random.randint(range_min, range_max, points_count)
y = np.random.randint(range_min, range_max, points_count)
z = np.random.randint(range_min, range_max, points_count)

points = [[x[i], y[i], z[i]] for i in range(points_count)]

clusters = KMeans(2).fit(points).labels_

colors = ['red' if clusters[i] == 1 else 'blue' for i in range(points_count)]

svc = SVC(kernel='linear')
svc.fit(points, clusters)

space = np.linspace(range_min, range_max)
xx, yx = np.meshgrid(space, space)

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=colors, size=point_size)))
fig.add_trace(go.Surface(x=xx, y=yx, z=get_z_coordinate_by_formula(xx, yx)))
fig.show()