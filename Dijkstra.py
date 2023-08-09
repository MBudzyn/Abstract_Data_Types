import heapq
class Edge:
    def __init__(self,movingDistance, startVertex, targetVertex):
        self.movingDistance = movingDistance
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node:
    def __init__(self, name):
        self.name = name
        self.edgesToNeighbours = []
        self.visited = False
        self.predecessor = None
        self.minDistanceToCome = float("inf")

    def __lt__(self, otherNode):
        return self.minDistanceToCome < otherNode.minDistanceToCome

    def addEdge(self,movingDistance,destinationVertex):
        newEdge = Edge(movingDistance,self,destinationVertex)
        self.edgesToNeighbours.append(newEdge)

class Dijkstra:
    def __init__(self):
        self.heap = []
    def calculateMinDistance(self,startVertex,endVertex):
        startVertex.minDistanceToCome = 0
        heapq.heappush(self.heap,startVertex)
        while self.heap:
            currentVertex = heapq.heappop(self.heap)
            currentVertex.visited = True
            for edge in currentVertex.edgesToNeighbours:
                if not edge.targetVertex.visited:
                    if edge.targetVertex.minDistanceToCome > currentVertex.minDistanceToCome + edge.movingDistance:
                        edge.targetVertex.minDistanceToCome = currentVertex.minDistanceToCome + edge.movingDistance
                        heapq.heappush(self.heap, edge.targetVertex)
                        edge.targetVertex.predecessor = currentVertex


        return endVertex.minDistanceToCome

def dijkstraTest():
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")

    nodeA.addEdge(6, nodeB)
    nodeA.addEdge(9, nodeD)
    nodeA.addEdge(10, nodeC)

    nodeB.addEdge(16, nodeE)
    nodeB.addEdge(13, nodeF)
    nodeB.addEdge(5, nodeD)

    nodeC.addEdge(6, nodeD)
    nodeC.addEdge(5, nodeH)
    nodeC.addEdge(21, nodeG)

    nodeD.addEdge(8, nodeF)
    nodeD.addEdge(7, nodeH)

    nodeE.addEdge(10, nodeG)

    nodeF.addEdge(4, nodeE)
    nodeF.addEdge(12, nodeG)

    nodeH.addEdge(2, nodeF)
    nodeH.addEdge(14, nodeG)


    dijkstra = Dijkstra()
    print(dijkstra.calculateMinDistance(nodeD, nodeG))
    actualVertex = nodeG
    result = []
    while actualVertex is not None:
        result.insert(0,actualVertex.name)
        actualVertex = actualVertex.predecessor
    print(result)



dijkstraTest()