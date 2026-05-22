from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[i]:
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

        labels = {0: 'S\n(0)', 1: 'A\n(1)', 2: 'B\n(2)', 3: 'C\n(3)', 
                  4: 'D\n(4)', 5: 'E\n(5)', 6: 'H\n(6)', 7: 'G\n(7)'}

        plt.figure(figsize=(8, 7))
        
        pos = {
            0: (0, 3),
            1: (-1.5, 2),
            2: (0, 2),
            3: (1.5, 2),
            4: (-2, 1),
            5: (-1, 1),
            6: (-2, 0),
            7: (-1, 0)
        }

        nx.draw_networkx_nodes(G, pos, node_size=900, node_color='teal', edgecolors='black')
        nx.draw_networkx_edges(G, pos, width=2, edge_color='black')
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=11, font_color='white', font_weight='bold')

        plt.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 7)

    print("DFS - Duyệt tìm kiếm từ vertex 0 (Đỉnh S):")
    g.DFS(0)
    g.drawGraph()