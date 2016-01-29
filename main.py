from graph import Graph


def menu():
    print "========================"
    print "=         Main         ="
    print "========================"

    print "1 - Show nodes"
    print "2 - Show adjacency matrix"
    print "3 - Search... "


def setup_graph():
    graph = Graph(5)

    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")

    graph.add_arc_with_labels("a", "b")
    graph.add_arc_with_labels("a", "c")
    graph.add_arc_with_labels("c", "d")
    graph.add_arc_with_labels("c", "e")
    graph.add_arc_with_labels("b", "e")

    return graph


def main():
    graph = setup_graph()
    option = 0

    while option != -1:
        menu()
        option = input("Type your option: ")

        if option == 1:
            graph.show_nodes()

        elif option == 2:
            graph.show_adjacency_matrix()

        elif option == 3:
            label_from = raw_input("Label of from node:")
            label_to = raw_input("Label of to node: ")

            graph.depth_search(label_from, label_to)

main()
