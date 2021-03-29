import open_files as of
import insert_graph as ig
import breadth_first_search as bfs
import depth_first_search as dfs
import show_graph

graph = {}

def option_zero():
    print("\tHasta pronto!!!")
    exit()

def option_one():
    global graph
    graph = ig.create_nodes()
    show_graph.show_graph(graph)

def option_two():
    global graph
    graph = of.create_diccionary()
    show_graph.show_graph(graph)

def option_three():
    bfs.breadth_first_serch(graph)

def option_four():
    dfs.depth_first_search(graph)

def option_five():
    show_graph.show_graph(graph)

def show_menu():
    print("| ========================== Menu ============================ |")
    print("\t1. - Insertar Grafo")
    print("\t2. - Leer Grafo de CSV")
    print("\t3. - Breadth first search")
    print("\t4. - Depth first search")
    print("\t5. - Mostrar Grafo")
    print("\t0. - Salir")
    print("| ============================================================ |")
def main():
    while True:
        show_menu()
        a = int(input("\tIntroduzca la opcion que desea: "))
        if   a == 1: option_one()
        elif a == 2: option_two()
        elif a == 3: option_three()
        elif a == 4: option_four()
        elif a == 5: option_five()
        elif a == 0: option_zero()

if __name__ == "__main__":
    main()
