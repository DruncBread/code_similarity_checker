import networkx
from similarity_index_of_label_graph_package import similarity_index_of_label_graph_class

from networkx.generators.directed import gnr_graph
from networkx.generators import spectral_graph_forge
import numpy

g1 = networkx.Graph()
g1.add_node(0)
g1.add_node(1)
g1.add_edge(0, 1)

g2 = networkx.Graph()

g2.add_node(0)
g2.add_node(1)
g2.add_edge(1,0)

similarity_index_of_label_graph = similarity_index_of_label_graph_class()
sim_index = similarity_index_of_label_graph(g1, g2)
print(sim_index)
