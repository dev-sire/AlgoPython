class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(v2)
            self.vertices[v2].add_neighbor(v1)
            return True
        else:
            return False

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

# Create a graph with 4 vertices and 5 edges
graph = Graph()
for i in range(4):
    graph.add_vertex(Vertex(i))
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)