#-*- coding: utf-8 -*-

from Graph import *
from Node import *
from Edge import *

g = Graph()

nodes = []
for i in range(5):
    node = g.addNode("node " + str(i))
    nodes.append(node)

g.addEdge(nodes[0], nodes[2])
g.addEdge(nodes[2], nodes[4])
g.addEdge(nodes[0], nodes[3])

#g.show()

for n in nodes:
    print n
