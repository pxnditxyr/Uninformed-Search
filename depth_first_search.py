def dfs(graph, current, visited):
    if current not in visited:
        print(f"Current: {current}")
        visited.append(current)
        for j in graph[current][::-1]:
            current = j[0]
            dfs(graph, current, visited)

def depth_first_search(graph):
    visited = []
    source_node = input("\tIngresa el nodo source_node: ")
    print("\tLista de recorrido en Profundidad\n")
    current = source_node
    for i in graph:
        if current not in visited:
            dfs(graph, current, visited)
        else:
            if i not in visited:
                current = i
                dfs(graph, current, visited)

