#-*- coding: utf-8 -*-

from Attributes import *

class Node:
    """
    """

    ID = 0

    def __init__(self):
        """
        """

        self.id = Node.ID
        Node.ID += 1

        self.edges = []

        self.attr = Attributes()
