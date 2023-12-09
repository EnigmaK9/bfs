import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited_nodes = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited_nodes.append(node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited_nodes

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)
pos = nx.spring_layout(G)

visited_order = bfs(graph, 'A')

# Dibujar el grafo con el orden de visita resaltado
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12)
labels = {node: node for node in G.nodes()}
edge_labels = {(u, v): f"{u}-{v}" for u, v in G.edges()}

nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

nx.draw(G, pos, nodelist=visited_order, node_color='lightgreen', node_size=500)

plt.title("Recorrido BFS en el Grafo")
plt.show()
