# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


from . import Attribute

class Item(object):
    """
    """

    ID = 0

    def __init__(self, id=None):
        if id is None:
            self.id = str(Item.ID)
            Item.ID += 1
        else:
            self.id = id
        self.attr = {}

    def __str__(self):
        """
        """

        s = ""

        s += "ID: %i" % self.id
        s += "\n"

        for a in self.attr:
            s += "%s : %s" % (self.attr[a].name, str(self.attr[a].value))
            s += "\n"

        return s

    def __getitem__(self, name):
        """
        """

        return self.attr[name].value

    def set_attribute(self, name, value, type):
        """
        """

        self.attr[name] = Attribute(name, value, type)

    def attributes(self):
        """
        """

        return self.attr
