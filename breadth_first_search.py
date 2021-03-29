def breadth_first_serch(graph):
    visited, tour_queue = [], []
    source_node = input("\tIngresa el nodo source_node: ")
    print("\tLista de recorrido en anchura\n")
    tour_queue.append(source_node)
    while tour_queue:
        current = tour_queue.pop(0)
        if current not in visited:
            print("Vertice Actual -> ", current)
            visited.append(current)
        for key, lista in graph[current]:
            if key not in visited:
                tour_queue.append(key)
    print()
    return tour_queue
