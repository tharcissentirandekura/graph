class Edge:

    def __init__(self, source, destination, label):
        self.source = source
        self.destination = destination
        self.label = label

    def __str__(self):
        return self.label

    def __repr__(self):
        return str(self)
    
    def getDestination(self):
        return self.destination
    
    def getSource(self):
        return self.source
    
    def getLable(self):
        return self.label