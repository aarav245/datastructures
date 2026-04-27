#class to represent each node
class Graph():
    def __init__(self):
        self.graph = {}
    def addnode(self, data):
        if data not in self.graph:
            self.graph[data] = []
    def edge(self,node1,node2,directed = False):
        if node1 not in self.graph:
            self.add(node1)
        if node2 not in self.graph:
            self.add(node2)
        #adding edge from node1 to node2
        self.graph[node1].append(node2)
        #if undirected graph
        if not directed:
            self.graph[node2].append(node1)
    #function to display
    def display(self):
        for node in self.graph:
            print(f"{node}:{self.graph[node]}")
    #function to check if the node exists
    def check(self,node):
        return node in self.graph
    #function to delete node
    def delnode(self,node):
        #checking if node exists
        if node not in self.graph:
            print("Node does not exist!")
        else:
            for i in self.graph:
                if node in self.graph[i]:
                    self.graph[i].remove(node)
        del self.graph[node]
    #function to delete an edge
    def deledge(self,node1,node2,directed = False):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        else:
            print("Edge does not exist!")
        if not directed:
            if node2 in self.graph and node1 in self.graph[node2]:
                self.graph[node2].remove(node1)
    def cleargraph(self):
        self.graph.clear()
#actual creation of graph
graph1 = Graph()
graph1.addnode("g")
graph1.addnode("h")
graph1.addnode("i")
graph1.addnode("p")
graph1.addnode("a")
graph1.addnode("d")
graph1.addnode("s")
graph1.addnode("f")
#adding edge
graph1.edge("g","h")
graph1.edge("h","f")
graph1.edge("i","s")     
graph1.edge("f","d")
graph1.edge("d","a")
graph1.edge("a","s")  
graph1.edge("p","i")
graph1.edge("s","d")  
print("inital graph")
graph1.display()
user1 = input("which node do you want to check for existance?")
user2 = graph1.check(user1)
print(user2)
#delete an edge
userdelnode1 = input("What node would you like to delete? (deledge)")
userdelnode2 = input("What node would you like to delete?")
graph1.deledge(userdelnode1,userdelnode2)
graph1.display()
delnode1 = input("What node would you like to delete? (delnode)")
graph1.delnode(delnode1)
graph1.display()
clearuser = int(input("Would you like to clear the graph? 1 for yes"))
if clearuser == 1:
    graph1.cleargraph()
    print("Graph has been cleared")
graph1.display()

