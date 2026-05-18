def bfspathe(graph,startnode,endnode):
    visited = set()
    queue = [startnode]
    visited.add(startnode)
    while queue:
        currentnode = queue.pop(0)
        print("Visiting: ", currentnode)
        if currentnode == endnode:
            return True
        for neighbor in graph[currentnode]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

graph = {
    0: [1,2],
    1: [2],
    2: [0,3],
    3: [3]
}

start = 0
end = 3
result = bfspathe(graph,start,end)
print("Path exists ",result)

