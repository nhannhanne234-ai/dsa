from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (max(self.graph) + 1)
        self.DFSUtil(v, visited)
        print()

    def drawGraph(self):
        G = nx.Graph()

        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        plt.figure(figsize=(8, 6))
        
        pos = nx.spring_layout(G, seed=42) 

        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='orange', edgecolors='black')
        nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold', font_family='sans-serif')

        plt.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(4, 2)
    g.addEdge(1, 4)
    g.addEdge(4, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(3, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(4, 5)

    print("DFS - Duyệt tìm kiếm từ vertex 0:")
    g.DFS(0)
    g.drawGraph()