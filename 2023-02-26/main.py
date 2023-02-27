'''
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
'''''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SL_List():
    def __init__(self):
        self.head = None

    def display(self):
        output = ""

        node = self.head

        output += str(node.value)

        while node.next:
            output += " -> " + str(node.next.value)
            node = node.next
        print(output)

    def swap_every_two(self):
        temp_node = self.head

        while (temp_node and temp_node.next):
            temp_node.value, temp_node.next.value = temp_node.next.value, temp_node.value
            temp_node = temp_node.next.next

size = int(input("Input size of Singly Linked List: "))

nodes = [Node(i) for i in range(1, size+1)]

sl_list = SL_List()
sl_list.head = nodes[0]

for i in range(size-1):
    nodes[i].next = nodes[i+1]

print("Before swapping: ")
sl_list.display()

print("After swapping:")
sl_list.swap_every_two()
sl_list.display()