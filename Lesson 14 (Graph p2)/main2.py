#Finding isolated nodes
graph = {
    0:[1],1:[0,2],2:[1],3:[],4:[]
}
def isolatednodes(graph):
    isolated = []
    for node in graph:
        if len(graph[node]) == 0:
            isolated.append(node)
    return isolated
result = isolatednodes(graph)
print("Isolated nodes are: ", result)