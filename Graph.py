class Graph:
    def __init__(self,gdict=None):
        if gdict == None:
            self.gdict = {}
        else:
            self.gdict = gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def BFS(self,startVertex):
        visited = set()
        visited.add(startVertex)
        toVisitQueue = [startVertex]
        while toVisitQueue:
            startVertex = toVisitQueue.pop(0)
            print(startVertex, end=" -> ")
            for ver in self.gdict[startVertex]:
                if ver not in visited:
                    visited.add(ver)
                    toVisitQueue.append(ver)
    def DFS(self,startVertex):
        visited = set()
        visited.add(startVertex)
        toVisitStack = [startVertex]
        while toVisitStack:
            startVertex = toVisitStack.pop()
            print(startVertex, end=" -> ")
            for ver in self.gdict[startVertex]:
                if ver not in visited:
                    visited.add(ver)
                    toVisitStack.append(ver)


def BFSandDFSTest():
    customDict = {"a": ["b", "c"],
                  "b": ["a", "d", "e"],
                  "c": ["a", "e"],
                  "d": ["b", "e", "f"],
                  "e": ["d", "f", "c"],
                  "f": ["d", "e"]
                  }
    customGraph = Graph(customDict)
    print(customGraph.gdict)
    customGraph.DFS("c")
    print()
    customGraph.DFS("c")
    print()
    customGraph.BFS("c")
    print()
    customGraph.BFS("c")

BFSandDFSTest()


