# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


from . import Item
from . import NodeAttribute


class Node(Item):
    """
    """

    def __init__(self, id=None):
        """
        """

        super(Node, self).__init__(id)

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

    def set_attribute(self, name, value, type):
        """
        """
        self.attr[name] = NodeAttribute(name, value, type)
