Overview
========

GraphML
-------

`GraphML`_ is a comprehensive and easy-to-use file format for
graphs. It consists of a language core to describe the structural
properties of a graph and a flexible extension mechanism to add
application-specific data. Its main features include support of

* directed, undirected, and mixed graphs,
* hypergraphs,
* hierarchical graphs,
* graphical representations,
* references to external data,
* application-specific attribute data, and light-weight parsers.

Unlike many other file formats for graphs, GraphML does not use a
custom syntax. Instead, it is based on XML and hence ideally suited as
a common denominator for all kinds of services generating, archiving,
or processing graphs.

.. note::
   Above description is coming from GraphML official website:
   http://graphml.graphdrawing.org/.

PyGraphML
---------

PyGraphML is a small library designed to parse GraphML files. This
library has been written in Python. It's main feature are:

* reading GraphML file and getting consistant graph accessible in
  Python.
* write a graph object to a GraphML file.
* flexible attributes management.
* graph visualization using `NetworkX`_

Git deposit is available at http://github.com/hadim/pygraphml

What's next :

* Want to install PyGraphML ? go to :ref:`pygraphml-installation`.
* Want to learn how to use PyGraphML ? go to :ref:`pygraphml-usage`.

.. _GraphML: http://graphml.graphdrawing.org/
.. _NetworkX: https://github.com/hadim/pygraphml
