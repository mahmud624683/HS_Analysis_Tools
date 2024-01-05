import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self):
        # Create a directed graph
        self._G = nx.DiGraph()

        # Private attributes for nodes and edges
        self._nodes = []
        self._edges = []

    def add_node(self, node):
        # Add a single node to the graph
        self._G.add_node(node)
        self._nodes.append(node)

    def add_edge(self, source, target):
        # Add a single directed edge to the graph
        self._G.add_edge(source, target)
        self._edges.append((source, target))

    def show_graph(self):
        # Draw the graph
        pos = nx.drawing.nx_pydot.graphviz_layout(self._G, prog='dot')
        pos_attrs = {node: (-coords[1], coords[0]) for node, coords in pos.items()}

        nx.draw(
            self._G,
            pos=pos_attrs,
            with_labels=True,
            font_weight='bold',
            node_size=700,
            node_color='skyblue',
            font_size=10,
            edge_color='gray',
            linewidths=1,
            arrowsize=15,
            connectionstyle='arc3,rad=0.1'
        )

        # Display the graph
        plt.show()


class Node:
    def __init__(self, name, node_type):
        self._name = name
        self._node_type = node_type
        self._input_list = []
        self._output_list = []
        self._depth = 0
        self._func = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
    
    @property
    def func(self):
        return self._func
    
    @func.setter
    def func(self, value):
        self._func = value

    @property
    def input_list(self):
        return self._input_list
    
    
    @property
    def output_list(self):
        return self._output_list

    def add_input(self, input_node):
        self._input_list.append(input_node)

    def add_output(self, output_node):
        self._output_list.append(output_node)

    def append_inputlist(self, input_nodes):
        self._input_list += input_nodes

    def append_outputlist(self, output_nodes):
        self._output_list += output_nodes
    
    def print_node(self):
        print("name: ", self._name)
        print("gate type: ", self._node_type)
        print("input pins: ", self._input_list)
        print("output pins: ", self._output_list)
        print("function: ", self._func)
        print("depth: ", self._depth)
        print("----------------------")
