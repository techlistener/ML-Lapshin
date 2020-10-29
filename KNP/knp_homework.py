import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import networkx as nx


def first_connection(weight, tree):
    connect_pnt = [0 for i in range(n)]
    minim = weight[0][1]
    i_min, j_min = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if minim > weight[i][j]:
                minim = weight[i][j]
                i_min, j_min = i, j
    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1
    return connect_pnt


def lync_all(weight, tree, connect_pnt):
    minim = sys.maxsize
    i_min, j_min = None, None
    for i in range(n):
        if connect_pnt[i] == 1:
            for j in range(n):
                if connect_pnt[j] == 0:
                    if minim > weight[i][j]:
                        minim = weight[i][j]
                        i_min, j_min = i, j
    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


def delete_connection(tree):
    maxim = 0
    i_max = j_max = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tree[i][j] > maxim:
                maxim = tree[i][j]
                i_max, j_max = i, j
    tree[i_max][j_max] = tree[j_max][i_max] = 0


n = 15
k = 3

weight = [[0 for i in range(n)] for i in range(n)]
for i in range(0, n):
    for j in range(i + 1, n):
        weight[i][j] = np.random.randint(1, 100)
        weight[j][i] = weight[i][j]

print("Defined weights:")
for i in range(0, n):
    print(weight[i])

tree = [[0 for i in range(n)] for j in range(n)]
for i in range(0, n):
    print(tree[i])
connect_pnt = first_connection(weight, tree)
while 0 in connect_pnt:
    lync_all(weight, tree, connect_pnt)
for i in range(k - 1):
    delete_connection(tree)

graph = nx.Graph(strict=False)
for i in range(0, n):
    graph.add_node(i)
for i in range(0, n):
    for j in range(0, n):
        if tree[i][j] == 0:
            continue
        graph.add_edge(i, j, weight=tree[i][j])
        tree[i][j] = tree[j][i] = 0
nx.draw_circular(graph, with_labels=True)
pos = nx.circular_layout(graph)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)
plt.show()