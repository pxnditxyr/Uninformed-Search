
def enter_neighbors(graph_node):
    n_neighbors = int(input(f"Introduzca el numero de vecinos del nodo {graph_node}: "))
    neighbors = []
    for i in range(n_neighbors):
        node_neighbor = input("Nodo Vecino: ")
        weight_neighbor = float(input("Peso de arista: "))
        neighbors.append((node_neighbor, weight_neighbor))
    return neighbors
def create_nodes():
    n_nodes = int(input("Introduzca el numero de vecinos de nodos que desea: "))
    nodes = {}
    for i in range(n_nodes):
        node = input(f"Introduzca la clave del nodo {i}: ")
        neighbors = enter_neighbors(node)
        nodes[node] = neighbors
    return nodes
