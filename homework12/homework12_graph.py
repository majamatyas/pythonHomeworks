
#Exercise 12.2

import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(n=6, m=7)  

plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=14, font_color='black')
plt.title("Random Undirected Graph with 6 Nodes")
plt.show()
