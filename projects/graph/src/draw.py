"""
General drawing methods for graphs using Bokeh.
"""

from random import choice, random

from bokeh.io import output_file, show
from bokeh.models import (Circle, ColumnDataSource, GraphRenderer, LabelSet,
                          StaticLayoutProvider)
from bokeh.plotting import figure
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, title='Graph', width=10, height=10,
                 show_axis=False, show_grid=False, circle_size=35):

        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(
            0, width), y_range=(0, height))

        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

        v_names = [v for v in self.pos.keys()]
        v_x = [v[0] for v in self.pos.values()]
        v_y = [v[1] for v in self.pos.values()]
        labels_source = ColumnDataSource(data=dict(v_names=v_names, v_x=v_x, v_y=v_y))
        labels = LabelSet(source=labels_source, x='v_x',
                          y='v_y', text='v_names')
        self.plot.add_layout(labels)

    def _get_random_colors(self):
        colors = []

        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)

        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""

        for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('D', 'E')

bg = BokehGraph(graph)
# bg.show()
print(bg.pos)
print(bg.pos.keys())
names = [name for name in bg.pos.keys()]
print(names)

