from graphVisualizer import GraphVisualizer

if __name__ == "__main__":
    # Create an instance of GraphVisualizer
    graph_visualizer = GraphVisualizer()

    # Add nodes and edges
    nodes = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    edges = [('x1', 'x2'), ('x1', 'x3'), ('x2', 'x4'), ('x2', 'x5'), ('x2', 'x6'), ('x3', 'x4'), ('x3', 'x6')]

    for node in nodes:
        graph_visualizer.add_node(node)

    for edge in edges:
        graph_visualizer.add_edge(edge[1], edge[0])

    # Show the graph
    graph_visualizer.show_graph()