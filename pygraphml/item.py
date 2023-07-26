# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from pygraphml import Attribute


class Item(object):
    """
    """

    ID = 0

    def __init__(self, node_id=None):
        if node_id is None:
            self.id = str(Item.ID)
            Item.ID += 1
        else:
            self.id = node_id
        self._attr: dict[str, Attribute] = {}

    def __str__(self):
        """
        """

        s = ""

        s += "ID: {}".format(self.id)
        s += "\n"

        for a in self._attr:
            s += "{} : {}".format(self._attr[a].name, str(self._attr[a].value))
            s += "\n"

        return s

    def __setitem__(self, name: str, value):
        """
        """

        self._attr[name] = Attribute(name, value)

    def __getitem__(self, name: str):
        """
        """

        return self._attr[name].value

    def attributes(self) -> dict[str, Attribute]:
        """
        """

        return self._attr
