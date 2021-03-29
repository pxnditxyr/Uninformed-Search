import pandas as pd
import numpy as np

graph_pd = pd.read_csv("graph.csv", header = None)
graph_np = np.array(graph_pd)

def create_diccionary():
    my_graph = {}
    for i in range(len(graph_np)):
        my_tuple = []
        if i != 0:
            for j in range(len(graph_np[0])):
                if j != 0 and graph_np[i][j] != '0' and graph_np[i][j] != '9999':
                    my_tuple.append((graph_np[0][j], float(graph_np[i][j])))
            my_graph[graph_np[i][0]] = my_tuple
    return my_graph
