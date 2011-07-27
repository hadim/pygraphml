#-*- coding: utf-8 -*-

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
    
