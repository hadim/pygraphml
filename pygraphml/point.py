# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


import math

class Point():
    """
    """

    def __init__(self, x = 0, y = 0, z = 0):
        """
        """

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def vectorize(self, point):
        """
        """

        p = Point()

        p.x = self.x - point.x
        p.y = self.y - point.y
        p.z = self.z - point.z

        return p

    def __mul__(self, point):
        """
        Cross product
        """

        p = Point()

        p.x = self.y * point.z - self.z * point.y
        p.y = self.z * point.x - self.x * point.z
        p.z = self.x * point.y - self.y * point.x

        return p

    def __str__(self):
        """
        """

        s = ""

        s += "x : %f" % self.x
        s += "\n"

        s += "y : %f" % self.y
        s += "\n"

        s += "z : %f" % self.z
        s += "\n"

        return s
