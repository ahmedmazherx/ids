# 17 April 2024
# CSC461 – Assignment3 – IDS – Graph Analysis
# Ahmed Mazher
# fa20-bse-046
# Using the networkx library in Python, create an undirected graph described by the adjacency matrix shown below. Once the graph is constructed, draw it to see if there is a loop in the graph?

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Assuming you've already installed networkx via pip

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

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold', font_size=14)
plt.title('Undirected Graph')
plt.show()
