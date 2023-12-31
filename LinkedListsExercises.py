from random import *
class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next
    def __str__(self):
        result = [str(x.value) for x in self]
        return " -> ".join(result)

    def __len__(self):
        result = 0
        iter_node = self.head
        while iter_node:
            result +=1
            iter_node = iter_node.next
        return result

    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self.tail

    def generate(self, n, min_number,max_number):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_number,max_number))

LL = LinkedList()