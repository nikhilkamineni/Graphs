#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Individual Vertex class"""
    def __init__(self, label):
        self.label = label


class Graph:
    """Represent a graph as a dict of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """ Add a new vertex, optionally with edges to other vertices"""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between to vertices"""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')

        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)


