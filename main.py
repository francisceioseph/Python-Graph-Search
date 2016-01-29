from graph import Graph


def menu(graph):

    print "========================"
    print "=         Main         ="
    print "========================"

    if graph is None:
        print "1 - Create a graph"
    else:
        print "2 - Insert a node with label"
        print "3 - Insert an arc"
        print "4 - Show nodes"
        print "5 - Show adjacency matrix"


def main():
    graph = None
    option = 0

    while option != -1:
        menu(graph)
        option = input("Type your option: ")

        if option == 1 and graph is None:
            max_size = input("Enter the graph max size: ")
            graph = Graph(max_size)
        else:
            if option == 2:
                label = raw_input("Node label:")
                graph.add_node(label)

            elif option == 3:
                label_from = raw_input("Label of from node:")
                label_to = raw_input("Label of to node: ")

                graph.add_arc_with_labels(label_from, label_to)

            elif option == 4:
                graph.show_nodes()

            elif option == 5:
                graph.show_adjacency_matrix()


main()
