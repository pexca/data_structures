class Node:

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)  # will try to return a printable version of an attribute


node = Node('test')  # pass a string to the 'cargo' attribute


# let's make a list with more than one node; pass integers to the 'cargo' attribute
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
nodeX = node
# link the nodes
node1.next = node2
node2.next = node3
node3.next = nodeX


def print_list(node):
    lst = []
    while node:
        lst.append(node)  # or simply print(node)
        node = node.next
    print(lst)

print_list(node1)


def print_backward(list):  # this prints out our linked list in reverse order
    if list is None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print(head)

print_backward(node1)


def removeSecond(list):
    if list is None:
        return
    first = list
    second = list.next
    # make the first node refer to the third
    first.next = second.next
    # separate the second node from the rest of the list
    second.next = None
    return second




