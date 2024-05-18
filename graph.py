from Vertex import Vertex
from Edge import Edge

class Graph:
    
    def __init__(self):
        self.graphMap = {}

        self.vertexSize = 0
        self.edgeSize = 0

    def addVertex(self, name):
        vertex = Vertex(name)
    
        if vertex.name not in self.graphMap:
            self.graphMap[vertex.name] = []
            self.vertexSize += 1
        return vertex.name

            
    
    def  addEdge(self,source,destination,label):
        edges = self.graphMap.get(source)

        print(source ,"edges :"  , edges)

        if edges is None:
            edges = []
            self.graphMap[source] = edges

        edge = Edge(source,destination,label)
        edges.append(edge)
        self.edgeSize +=1


    def containVertex(self,vertex):

        return vertex in self.graphMap
    
    def getVertices(self):

        allVertices = []

        for vertex in self.graphMap.keys():
            allVertices.append(vertex)
        return allVertices
    
    def  getEdge(self,source,destination):

        Edges = self.graphMap.get(source)

        for edge in Edges:
            if edge.getDestination() == destination:
                return edge
            
        destEdges = self.graphMap.get(destination) 

        for edge in destEdges:
            if edge.getDestination() == destination:
                return edge  
        return None


    
def main():

    graph = Graph()
    v1 = graph.addVertex('tharcisse')
    v2 = graph.addVertex('kelig')
    v3 = graph.addVertex('menard')

    graph.addEdge(v1, v2, 'thar-kelig')
    graph.addEdge(v2, v3, 'kelig-menard')
    graph.addEdge(v3, v1, 'menard-tharcisse')

    print(graph.graphMap)


if __name__ == '__main__':
    main()



    


    
    