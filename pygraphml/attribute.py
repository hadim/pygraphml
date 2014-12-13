# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


class Attribute:
    """
    """

    def __init__(self, name, value, type = "string"):
        """
        """

        self.name = name
        self.value = str(value)
        self.type = type

    def __str__(self):
        """
        """

        s = ""
        s += "%s : %s" % (self.name, str(self.value))
        return s

