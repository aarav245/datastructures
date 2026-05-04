graph = {
    1:[2],2:[1,3],3:[2,4],4:[3,5],5:[4]
}
def count_neighbors(graph,node):
    if node not in graph:
        return 0
    neighbors = graph[node]
    count = len(neighbors)
    return count

#result = count_neighbors(graph, 2)
#print("Number of neighbors of Node 2: ", result)

nodeinput = int(input("Enter the node you would like to search: "))
result = count_neighbors(graph,nodeinput)
print(f"Number of neighbors of Node {nodeinput} : {result}")