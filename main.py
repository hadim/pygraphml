#-*- coding: utf-8 -*-

from pygraphml.GraphMLParser import *
from pygraphml.Graph import *
from pygraphml.Node import *
from pygraphml.Edge import *

import sys

# parser = GraphMLParser()
# g = parser.parse(sys.argv[1])

# root = g.set_root_by_attribute("RootNode")
# #print g.root()

# for n in g.DFS_prefix():
#     print n

# #g.show(True)

g = Graph()

n1 = g.add_node("salut")
n2 = g.add_node("coucou")
n1['positionX'] = 555

g.add_edge(n1, n2)

parser = GraphMLParser()
parser.write(g, "ttest.graphml")

#g.show()
