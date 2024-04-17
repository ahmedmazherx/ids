# 17 April 2024
# CSC461 – Assignment3 – IDS – Graph Analysis
# Ahmed Mazher
# fa20-bse-046
# Assign random weights to the edges in the graph created in Q1. Once the weights are assigned, run Dijkstra to find out shortest path between A and B. Print both shortest path and the length of the shortest path.


import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Define your adjacency matrix
adjacency_matrix = np.array([
    [0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1]
])

# Create a graph from the adjacency matrix
G = nx.from_numpy_array(adjacency_matrix)

# Assign random weights to the edges and add them to the graph
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(1, 10)

# Use Dijkstra's algorithm to find the shortest path between node A (node 0) and node B (node 1)
shortest_path = nx.dijkstra_path(G, source=0, target=1, weight='weight')
shortest_path_length = nx.dijkstra_path_length(G, source=0, target=1, weight='weight')

# Print the shortest path and its length
print("Shortest path:", shortest_path)
print("Length of the shortest path:", shortest_path_length)
