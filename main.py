#-*- coding: utf-8 -*-

from pygraphml.GraphMLParser import *
from pygraphml.Graph import *
from pygraphml.Node import *
from pygraphml.Edge import *

import sys

parser = GraphMLParser()
g = parser.parse(sys.argv[1])

root = g.set_root_by_attribute("RootNode")
#print g.root()

for n in g.DFS_prefix():
    print n

#g.show(True)
