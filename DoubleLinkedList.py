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

    def createDLL(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    def __str__(self):
        result = ""
        for i in self:
            result += str(i.value) + " "
        return result


    def insert_on_index(self,index_from_0,value):
        new_node = Node(value)
        if index_from_0 < 0:
            return False
        elif self.head is None and index_from_0 ==0:
            self.createDLL(value)
            return True
        elif self.head is None:
            return False
        elif index_from_0 ==0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return True
        else:
            iter_node = self.head
            for i in range(index_from_0-1):
                if iter_node is None:
                    return False
                iter_node = iter_node.next
            if iter_node == self.tail:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                iter_node.next.prev = new_node
                new_node.next = iter_node.next
                iter_node.next = new_node
                new_node.prev = iter_node
            return True
def unit_test_insert():
    new_dll = DoubleLinkedList()
    new_dll.createDLL(10)
    print(new_dll)
    for i in range(11,20):
        new_dll.insert_on_index(i-10,i)
    print(new_dll)
    new_dll.insert_on_index(10,101)
    new_dll.insert_on_index(0,99)
    print(new_dll)
    new_dll.insert_on_index(3,100)
    print(new_dll)
    print(f"tail.value = {new_dll.tail.value}")
    print(f"head.value = {new_dll.head.value}")
    print(f"tail.prev.value = {new_dll.tail.prev.value}")
    print(f"head.next.value = {new_dll.head.next.value}")


unit_test_insert()



