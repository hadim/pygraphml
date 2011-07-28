.. _pygraphml-usage:

Usage example
=============

This page introduces you to PyGraphML. If you want to skip this step
and directly play with API documentation, go to
:ref:`pygraphml-reference`.

.. warning::
   Documentation is still incomplete. Be patient and do not hesitate
   to report bug.

Test if PyGraphML is working
----------------------------

First, open a Python console and try import PyGraphML

>>> import pygraphml
>>> 


If there is not ``ImportError`` message, PyGraphML is well detected by
your python installation.

Create a graph
--------------

Let's create a simple graph with 5 nodes and some edges between this
nodes::

  #-*- coding: utf-8 -*-

  from pygraphml.Graph import *
  from pygraphml.Node import *
  from pygraphml.Edge import *

  # Create graph

  g = Graph()

  n1 = g.add_node("A")
  n2 = g.add_node("B")
  n3 = g.add_node("C")
  n4 = g.add_node("D")
  n5 = g.add_node("E")

  g.add_edge(n1, n3)
  g.add_edge(n2, n3)
  g.add_edge(n3, n4)
  g.add_edge(n3, n5)

Visualize a graph with NetworkX
-------------------------------

If you have `NetworkX`_ installed, you can visualize the
graph.

.. note::
   Visualization is very basic and serves only to quickly check
   graph consistent.

It is very simple to visualize graph::

  g.show()

You should see something like that:

.. image:: graph.png
   :scale: 50 %
   :align: center

Write a graph into GraphML file
-------------------------------

Now you may want to write your graph into a GraphML file. This is a
way::

   #-*- coding: utf-8 -*-

   from pygraphml.GraphMLParser import *
   from pygraphml.Graph import *
   from pygraphml.Node import *
   from pygraphml.Edge import *

   # Create graph

   g = Graph()

   n1 = g.add_node("A")
   n2 = g.add_node("B")
   n3 = g.add_node("C")
   n4 = g.add_node("D")
   n5 = g.add_node("E")

   g.add_edge(n1, n3)
   g.add_edge(n2, n3)
   g.add_edge(n3, n4)
   g.add_edge(n3, n5)

   parser = GraphMLParser()
   parser.write(g, "myGraph.graphml")

.. warning::
   Don't forget to import ``GraphMLParser``

GraphML file should look like that

.. code-block:: xml

   <?xml version="1.0" ?>
       <graphml>
           <key attr.name="label" attr.type="string" id="label"/>
           <graph edgedefault="directed" id="">
               <node id="A"/>
               <node id="B"/>
               <node id="C"/>
               <node id="D"/>
               <node id="E"/>
               <edge source="A" target="C"/>
               <edge source="B" target="C"/>
               <edge source="C" target="D"/>
               <edge source="C" target="E"/>
           </graph>
       </graphml>

Read a graph from GraphML file
-------------------------------

Now let's learn how to read a graph from a GraphML file. We will take
the previous generated GraphML file, load it in Python and display it
with `NetworkX`_::

  parser = GraphMLParser()
  g = parser.parse("myGraph.graphml")

  g.show()

Nodes and edges attributes management
-------------------------------------

GraphML format has a flexible attributes management as PyGraphML. To
add an attribute to a node or an item, simply use Python power::

  g = Graph()
  n = g.add_node('label')
  
  # Add attribute
  n['color'] = 'red'

  # Read attribute
  print n['color']

All attributes will be copied in GraphML file. As well when you read a
GraphML file, attributes are available by the same way.

.. _NetworkX: https://github.com/hadim/pygraphml
