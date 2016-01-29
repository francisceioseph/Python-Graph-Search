from graph import Graph


def menu():
    print "========================"
    print "=         Main         ="
    print "========================"

    print "1 - Insert a node with label"
    print "2 - Insert an arc"
    print "3 - Show nodes"
    print "4 - Show adjacency matrix"


def setup_graph():
    graph = Graph(5)

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")

    graph.add_arc_with_labels("A", "B")
    graph.add_arc_with_labels("A", "C")
    graph.add_arc_with_labels("C", "D")
    graph.add_arc_with_labels("C", "E")
    graph.add_arc_with_labels("B", "E")

    return graph


def main():
    graph = setup_graph()
    option = 0

    while option != -1:
        menu(graph)
        option = input("Type your option: ")

        if option == 1:
            label = raw_input("Node label:")
            graph.add_node(label)

        elif option == 2:
            label_from = raw_input("Label of from node:")
            label_to = raw_input("Label of to node: ")

            graph.add_arc_with_labels(label_from, label_to)

        elif option == 3:
            graph.show_nodes()

        elif option == 4:
            graph.show_adjacency_matrix()


main()
