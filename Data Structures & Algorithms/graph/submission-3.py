class Graph:
    
    def __init__(self):
        self.nodes = {} # using adjacency list


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.nodes:
            self.nodes[src] = []
        if dst not in self.nodes:
            self.nodes[dst] = []
        if dst not in self.nodes[src]:
            self.nodes[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.nodes:
            return False
        if dst in self.nodes[src]:
            self.nodes[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        def checkPath(nodes, src, dst, visited):
            if src == dst:
                return True
            if src not in nodes:
                return False
            for neighbor in nodes[src]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if checkPath(nodes,neighbor, dst, visited):
                        return True

            return False
        visited = set([src])
        return checkPath(self.nodes, src, dst, visited)
