class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next



