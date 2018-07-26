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

    def search(self, start, target=None, method='bfs'):
        quack = [start]  # queue or stack depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            visited.add(current)
            quack.extend(self.vertices[current] - visited)

        return visited

    # def bfs(self, start, target=None):
    #     queue = [start]
    #     visited = set()

    #     while queue:
    #         current = queue.pop(0)
    #         visited.add(current)
    #         queue.extend(self.vertices[current] - visited)

    #     return visited

    # def dfs(self, start, target=None):
    #     stack = [start]
    #     visited = set()

    #     while stack:
    #         current = stack.pop()
    #         visited.add(current)
    #         stack.extend(self.vertices[current] - visited)

    #     return visited




