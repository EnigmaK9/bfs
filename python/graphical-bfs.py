import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

def bfs_animation(graph, start):
    visited = set()
    queue = deque([start])
    visited_nodes = []

    def update(num):
        plt.clf()
        node = visited_order[num]
        visited_nodes.append(node)
        visited.add(node)

        # Dibujar el grafo
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12)
        labels = {node: node for node in G.nodes()}
        edge_labels = {(u, v): f"{u}-{v}" for u, v in G.edges()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

        # Resaltar los nodos visitados
        nx.draw(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=500)

    G = nx.Graph(graph)
    visited_order = list(nx.bfs_tree(G, source=start))

    fig, ax = plt.subplots(figsize=(8, 6))

    ani = animation.FuncAnimation(fig, update, frames=len(visited_order), repeat=False)
    plt.title("Recorrido BFS en el Grafo")
    plt.show()

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs_animation(graph, 'A')

