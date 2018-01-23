class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

    def add_vertices(self, new_vertices):
        self.vertices += new_vertices

    def add_vertice(self, new_vertice):
        self.vertices += [new_vertice]

    def __repr__(self):
        res=""
        for vert in self.vertices:
            res+=str(vert.label)+"\n"
            for n_e in vert.next_edges:
                res+=str(n_e.__dict__)+"\n"
            res+="\n"

        return res

class Vertice:
    def __init__(self, label, next_edges=list()):
        self.label = label
        self.next_edges = list(next_edges)

    def add_next_edges(self, new_edges):
        self.next_edges += new_edges

    def add_next_edge(self, new_edge):
        self.next_edges += [new_edge]


class Edge:
    def __init__(self, cond, com, next_label):
        self.cond = cond
        self.com = com
        self.next_label = next_label


class Command:
    pass


class Boolean:
    pass


# Execution

if __name__ == "__main__":
    V1 = Vertice(1)
    V1.add_next_edge(Edge("X<=0", "skip", 2))
    V1.add_next_edge(Edge("not(X<=0)", "skip", 3))
    V2=Vertice(2)
    V2.add_next_edge(Edge("true", "X:=X", 4))
    V3=Vertice(3)
    V3.add_next_edge(Edge("true", "X:=1-X", 4))
    V4 = Vertice(4)
    V4.add_next_edges([Edge("X=1", "skip", 5), Edge("not(X=1)", "skip", 6)])
    V5 = Vertice(5)
    V5.add_next_edge(Edge("true", "X:=1", "exit"))
    V6 = Vertice(6)
    V6.add_next_edge(Edge("true", "X:=X+1", "exit"))
    Vexit = Vertice("exit")
    Control_Graph = Graph([V1, V2, V3, V4, V5, V6, Vexit])
    print(Control_Graph)
