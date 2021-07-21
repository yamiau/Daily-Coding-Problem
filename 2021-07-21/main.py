from random import randint


# Classes


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.size() < 1:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def as_string(self):
        current_node = self.head
        string = ""
        while current_node is not None:
            string += str(current_node.value) + " -> "
            current_node = current_node.next
        return string


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# Functions


def sort(list):
    current = list.head

    while current is not None:
        next = current.next
        while next is not None:
            if current.value > next.value:
                temp = current.value
                current.value = next.value
                next.value = temp
            next = next.next
        current = current.next


def alt_low_high(list):
    sort(list)
    current = list.head.next
    next = current.next

    while next is not None:
        temp = current.value
        current.value = next.value
        next.value = temp
        current = next.next
        next = current.next


# Calls


my_list = LinkedList()

for i in range(10):
    node = Node(randint(1, 100))
    my_list.add(node)
    print("Added node with value: ", node.value)

print("\nList size: ", my_list.size())
print(my_list.as_string(), "\n")

alt_low_high(my_list)
print("Rearranged list:")
print(my_list.as_string())
