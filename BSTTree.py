
class BSTNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
def insertNode(rootNode,rootValue):
    if rootNode.value == None:
        rootNode.value = rootValue
    else:
        if rootValue <= rootNode.value:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(rootValue)
            else:
                insertNode(rootNode.leftChild, rootValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(rootValue)
            else:
                insertNode(rootNode.rightChild, rootValue)

def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    elif value < rootNode.value:
        rootNode.lefChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.value:
        rootNode.rightChild = deleteNode(rootNode.rightChild,value)
    else:
        if rootNode.leftChild is None:
            tmpNode = rootNode.rightChild
            rootNode = None
            return tmpNode
        elif rootNode.rightChild is None:
            tmpNode = rootNode.leftChild
            rootNode = None
            return tmpNode
        else:
            tmpValue = minValue(rootNode.rightChild).value
            rootNode.value = tmpValue
            rootNode.rightChild = deleteNode(rootNode.rightChild,tmpValue)
            return rootNode

def minValue(rootNode):
    iterNode = rootNode
    while iterNode.leftChild is not None:
        iterNode = iterNode.leftChild
    return iterNode

def printBST(rootNode):
    if rootNode is None:
        return
    printBST(rootNode.leftChild)
    print(rootNode.value,end = " ")
    printBST(rootNode.rightChild)


newBST = BSTNode(None)
insertNode(newBST,60)
insertNode(newBST,70)
insertNode(newBST,40)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,20)
insertNode(newBST,80)
insertNode(newBST,50)
insertNode(newBST,10)
printBST(newBST)
print()
deleteNode(newBST,40)

printBST(newBST)
