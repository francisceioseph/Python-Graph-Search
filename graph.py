from node import Node


class Graph:
    def __init__(self, max_size):
        self.max_size = max_size
        self.nodes = []
        self.adjacency_matrix = []

        for i in range(self.max_size):
            line = [0] * self.max_size
            self.adjacency_matrix.append(line)

    def number_of_nodes(self):
        return len(self.nodes)

    def add_node(self, label):
        node = Node(label)

        if self.number_of_nodes() < self.max_size:
            self.nodes.append(node)
        else:
            print "The graph is crowded."

    def add_arc(self, start, end):
        valid_range = range(0, self.max_size)

        if start in valid_range and end in valid_range:
            self.adjacency_matrix[start][end] = 1
            self.adjacency_matrix[end][start] = 1
        else:
            print "Invalid start/end"

    def add_arc_with_labels(self, label_start, label_end):
        node_start = [node for node in self.nodes if node.label == label_start].pop()
        node_end = [node for node in self.nodes if node.label == label_end].pop()

        start_index = self.nodes.index(node_start)
        end_index = self.nodes.index(node_end)

        self.add_arc(start_index, end_index)

    def show_node_at_index(self, node_number):
        print(self.adjacency_matrix[node_number].label)

    def show_nodes(self):
        print "========================"
        print "=    Nodes in Graph    ="
        print "========================"

        for node in self.nodes:
            print node
        print

    def show_node_by_label(self, label):
        found_label = None

        for node in self.nodes:
            if node.label == label:
                found_label = node.label

        print(found_label)

    def show_adjacency_matrix(self):
        print "==============================="
        print "=  Adjacency Matrix in Graph  ="
        print "==============================="

        print " ",

        for node in self.nodes:
            print node.label,
        print

        for i in range(self.number_of_nodes()):
            print self.nodes[i].label,
            for j in range(self.number_of_nodes()):
                print self.adjacency_matrix[i][j],
            print
