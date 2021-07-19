#Classes
class Tree:
    def __init__(self, ID):
        self.ID = ID
        self.root = None

    def root(self, node):
        if self.root == None and isinstance(node, Node):
            self.root = node
        else:
            print("Could not add root to tree ", self.ID, "!")

class Node:
    def __init__(self, parent, ID):
        self.parent = parent
        self.left = None
        self.right = None
        self.ID = ID

    def branch(self, node):
        if self.left == None and isinstance(node, Node):
            self.left = node
        elif self.right == None and isinstance(node, Node):
            self.right = node
        else:
            print("Could not add a branch to node ", node.ID, "!")
