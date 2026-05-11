#DFS and undirected

class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[] for i in range(n)]
    
    def addEdge(self,x,y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def dfsMain(self,node,visited):
        visited[node] = True
        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.dfsMain(neighbor,visited)
    
    def count_comp(self):
        visited = [False] * self.n
        count = 0
        for i in range(self.n):
            if not visited[i]:
                count += 1
                self.dfsMain(i,visited)
        return count

g = Graph(5)
g.addEdge(0,1)
g.addEdge(2,3)
print(g.count_comp())
    