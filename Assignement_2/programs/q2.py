import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1

gc.disable()
print("Before garbage collection:")
print(node1.data, node2.data, node3.data)
gc.enable()
gc.collect()

try:
    print("After garbage collection:")
    print(node1.data, node2.data, node3.data)
except NameError:
    print("Nodes are no longer accessible due to garbage collection.")