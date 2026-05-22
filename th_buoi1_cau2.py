from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, u):
        visited = set()

        queue = []

        visited.add(u)
        queue.append(u)

        while queue:
            u = queue.pop(0)
            print(u, end=' ')

            for i in self.graph[u]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        print()

    def drawGraph(self):
        G = nx.Graph()

        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42) 

        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
        nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=14, font_family='sans-serif', font_weight='bold')

        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(4, 8)
    g.addEdge(1, 0)
    g.addEdge(2, 0)
    g.addEdge(3, 0)
    g.addEdge(4, 1)
    g.addEdge(5, 1)
    g.addEdge(6, 2)
    g.addEdge(7, 3)
    g.addEdge(8, 4)

    print("BFS - duyệt tìm kiếm chiều rộng bắt đầu từ đỉnh 0:")
    g.BFS(0)
    g.drawGraph()