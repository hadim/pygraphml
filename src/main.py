#-*- coding: utf-8 -*-

from GraphMLParser import *
from Graph import *
from Node import *
from Edge import *

import sys

parser = GraphMLParser()
g = parser.parse(sys.argv[1])
g.show(True)
