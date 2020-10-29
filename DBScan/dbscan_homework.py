import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
import seaborn as sns


class Flag(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    UNKNOWN = -1


def get_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n = 100
x = np.random.randint(1, 100, n)
y = np.random.randint(1, 100, n)
eps, minPts = 12, 3
flags = []

for i in range(0, n):
    neighb = -1
    for j in range(0, n):
        if get_distance(x[i], y[i], x[j], y[j]) < eps:
            neighb += 1
    if neighb >= minPts:
        flags.append(Flag.GREEN.value)
    else:
        flags.append(Flag.UNKNOWN.value)
for i in range(0, n):
    if flags[i] == Flag.UNKNOWN.value:
        for j in range(0, n):
            if flags[j] == Flag.GREEN.value and get_distance(x[i], y[i], x[j], y[j]) < eps:
                flags[i] = Flag.YELLOW.value
                break
    if flags[i] == Flag.UNKNOWN.value:
        flags[i] = Flag.RED.value
clusters = np.zeros(n)
cl = 1
for i in range(0, n):
    if flags[i] == Flag.GREEN.value:
        if clusters[i] == 0:
            clusters[i] = cl
            cl += 1
        for j in range(0, n):
            if flags[j] == Flag.GREEN.value:
                if get_distance(x[i], y[i], x[j], y[j]) < eps:
                    clusters[j] = clusters[i]
            if flags[j] == Flag.YELLOW.value:
                min = 0
                for m in range(n):
                    if flags[m] == Flag.GREEN.value and min < get_distance(x[j], y[j], x[m], y[m]):
                        min = get_distance(x[j], y[j], x[m], y[m])
                if get_distance(x[i], y[i], x[j], y[j]) < eps and get_distance(x[i], y[i], x[j], y[j]) == min:
                    clusters[j] = clusters[i]

df = pd.DataFrame(columns={'x', 'y', 'clusters'})
df['x'] = [x[i] for i in range(0, n) if clusters[i] != 0]
df['y'] = [y[i] for i in range(0, n) if clusters[i] != 0]
df['clusters'] = [clusters[i] for i in range(0, n) if clusters[i] != 0]
x_r = [x[i] for i in range(0, n) if clusters[i] == 0]
y_r = [y[i] for i in range(0, n) if clusters[i] == 0]
facet = sns.lmplot(data=df, x='x', y='y', hue='clusters',fit_reg=False)
plt.scatter(x_r, y_r, c='r')
plt.show()
