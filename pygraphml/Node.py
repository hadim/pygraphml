#-*- coding: utf-8 -*-

from Item import *

class Node(Item):
    """
    """

    def __init__(self):
        """
        """

        super(Node, self).__init__()

        self._edges = []

    def edges(self, ):
        """
        """

        return self._edges
        

    def children(self):
        """
        """

        children = []
        for e in self._edges:
            if e.parent() == self:
                children.append(e.child())

        return children

    def parent(self):
        """
        """

        parent = []
        for e in self._edges:
            if e.child() == self:
                parent.append(e.parent())

        return parent
                               
