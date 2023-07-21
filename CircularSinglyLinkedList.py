class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    def CreateCSLL(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert(self, value, index_from_0): # method return True if the insertion was successful False in other case
        new_node = Node(value)
        if index_from_0 < 0 or index_from_0 > self.length: # wrong input data case
            return False
        if self.length == 0 and index_from_0 == 0: # empty CSLL case
            self.CreateCSLL(value)
            self.length +=1
            return True
        elif index_from_0 == 0: # prepend case
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            self.length +=1
            return  True
        elif index_from_0 == self.length: # append case
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
            self.length+=1
            return True
        else:
            iter_node = self.head
            for i in range(index_from_0 -1):
                iter_node = iter_node.next
            new_node.next = iter_node.next
            iter_node.next = new_node
            self.length +=1
            return True

    def traversalCSLL(self):
        if self.head is None:
            print("there is no items in SCLL")
        else:
            tmp_node = self.head
            print(tmp_node.value, end=" ")
            tmp_node = tmp_node.next
            while tmp_node != self.head:
                print(tmp_node.value, end=" ")
                tmp_node = tmp_node.next

    def searchCSLL(self,element):# method returns True if element exists in CSLL, False in other example
        if self.head is None:
            return False
        else:
            tmp_Node = self.head
            while tmp_Node != self.tail:
                if tmp_Node.value == element:
                    return True
                tmp_Node = tmp_Node.next
            if self.tail.value == element:
                return True
            else:
                return False


    def deleteCSLL(self, index_from_0): # method return True if the deletion was successful False in other case
        iter_node = self.head
        if index_from_0 < 0 or index_from_0 > self.length: # wrong input data case
            return False
        if self.length == 1 and index_from_0 == 0: # one element CSLL case
            self.head.next = None
            self.head = None
            self.tail = None
            self.length -=1
            return True
        elif index_from_0 == 0: # delete first element case
            self.head = self.head.next
            self.tail.next.next = None
            self.tail.next = self.head
            self.length -=1
            return  True
        elif index_from_0 == self.length -1: # delete last element case

            for i in range(index_from_0 - 1):
                iter_node = iter_node.next
            self.tail = iter_node
            iter_node.next.next = None
            iter_node.next = self.head
            self.length -=1
            return True
        else:
            for i in range(index_from_0 - 1):
                iter_node = iter_node.next
            prep_Node = iter_node.next.next
            iter_node.next.next = None
            iter_node.next = prep_Node
            self.length -= 1
            return True

def unit_test_insert():
    new_CSLL = CircularSinglyLinkedList()
    new_CSLL.CreateCSLL(10)

    for i in range(11, 16):
        new_CSLL.insert(i, i - 10)

    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.insert(5, 2)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.insert(6, 100)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.insert(7, 0)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    print(f"tail value: {new_CSLL.tail.value}")
    print(f"head value: {new_CSLL.head.value}")
    print(f"tail.next.value: {new_CSLL.tail.next.value}")
    print(f"length: {new_CSLL.length}")

def unit_test_delete():
    new_CSLL = CircularSinglyLinkedList()
    new_CSLL.CreateCSLL(20)
    new_CSLL2 = CircularSinglyLinkedList()
    new_CSLL2.CreateCSLL(30)
    print(new_CSLL2.deleteCSLL(0))
    print(f"length: {new_CSLL2.length}")

    for i in range(21, 29):
        new_CSLL.insert(i, i - 20)

    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.deleteCSLL(8)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.deleteCSLL(0)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    new_CSLL.deleteCSLL(4)
    for i in new_CSLL:
        print(i.value, end=" ")
    print()
    print(f"length: {new_CSLL.length}")

    print(f"tail value: {new_CSLL.tail.value}")
    print(f"head value: {new_CSLL.head.value}")
    print(f"tail.next.value: {new_CSLL.tail.next.value}")
    print(f"length: {new_CSLL.length}")

#unit_test_insert()
#unit_test_delete()














