from random import randint

#Classes


class Node:

    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):
    return abs(height(root.left) - height(root.right)) < 2


#Calls


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.left.left = Node(5)
root.left.left.right = Node(6)

if isBalanced(root):
    print("Tree #id", root.id, " is balanced!")
else:
    print("Tree #id", root.id, " is not balanced!")