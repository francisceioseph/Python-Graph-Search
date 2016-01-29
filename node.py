class Node:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return "Node: {0}".format(self.label)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        else:
            return NotImplemented

