# 
# Author: Miquel Anglada Girotto
# Contact: miquelangladagirotto [at] gmail [dot] com
#
# Script purpose
# --------------
# Draw a network and save. 
# Copied from https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_random_geometric_graph.html#sphx-glr-auto-examples-drawing-plot-random-geometric-graph-py.

import matplotlib.pyplot as plt
import networkx as nx
import os

# variables
dpi = 1000
plot_height = 1296 / dpi
plot_width = 3646 / dpi

# paths
ROOT='..'
images_dir = os.path.join(ROOT,'images')

# inputs

# outputs
blue_network_file = os.path.join(images_dir,'network_blue.eps')
red_network_file = os.path.join(images_dir,'network_red.eps')

G = nx.random_geometric_graph(50, 0.2)
g = plt.figure(figsize=(plot_width, plot_height), dpi = dpi)
nx.draw(G, node_size=20, alpha = 0.4)
plt.show()
g.savefig(blue_network_file, format = 'eps')

G = nx.random_geometric_graph(50, 0.2)
g = plt.figure(figsize=(plot_width, plot_height), dpi = dpi)
nx.draw(G, node_size=20, alpha = 0.4, node_color='red')
plt.show()
g.savefig(red_network_file, format='eps')


# nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
#nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()),
#                       node_size=80,
#                       node_color=list(p.values()),
#                       cmap=plt.cm.Reds_r)

#plt.xlim(-0.05, 1.05)
#plt.ylim(-0.05, 1.05)



print("Done!")