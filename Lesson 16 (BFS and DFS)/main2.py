#DFS

class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[] for i in range(n)]
    
    def createEdge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    
    def DFSrec(self,src,visited,res):
        res.append(src)
        visited[src] = True
        for node in self.adj[src]:
            if visited[node] == False:
                self.DFSrec(node,visited,res)
    
    def DFSmain(self,src):
        visited = [False] * self.n
        res = []
        self.DFSrec(src,visited,res)
        return res

u = int(input("How many nodes would you like to have? "))
graph1 = Graph(u)
e = int(input("How many edges would you like to add? "))
for i in range(e):
    x,y = map(int,list(input().split()))
    graph1.createEdge(x,y)

result = graph1.DFSmain(0)
print(result)