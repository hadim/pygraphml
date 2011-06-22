#-*- coding: utf-8 -*-

class Attributes:
    """
    """

    def __init__(self, **kwargs):
        """
        """

        self.attributes = kwargs

    def add_attr(self, **kwargs):
        """
        """

        self.attributes.update(kwargs)

    def __str__(self):
        """
        """

        return str(self.attributes)

    def __getitem__(self, name):
        """
        """

        return self.attributes[name]

if __name__ == '__main__':

    a = Attributes(test = "lll", i = 55)
    a.add_attr(p = 99)
        
    print a
    print a["test"]
