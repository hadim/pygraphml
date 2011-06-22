#-*- coding: utf-8 -*-

from Attributes import *

class Edge:
    """
    """

    ID = 0

    def __init__(self, node1, node2):
        """
        """

        self.id = Edge.ID
        Edge.ID += 1

        self.node1 = node1
        self.node2 = node2

        self.attr = Attributes()
