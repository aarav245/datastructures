#check if graph contains cycle
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.v = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def isCyclicUtil(self,v,recstack,visited):
        visited[v] = True
        recstack[v] = True
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor,visited,recstack) == True:
                    return True
            elif recstack[neighbor] == True:
                return True
        recstack[v] == False
        return False
    def isCyclic(self):
        visited = [False] * (self.v+1)
        recstack = [False]
        for node in range(self.v):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recstack) == True:
                    return True
        return False

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

if g.isCyclic() == 1:
    print("Graph has cycle")
else:
    print("Graph doesn't have a cycle")

g1 = Graph(4)
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(2,3)

if g1.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph doesn't have a cycle")