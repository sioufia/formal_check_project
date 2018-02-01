import re

from boolean_exp import Boolean_Exp
from command_exp import Command_Exp


class Graph:
    def __init__(self, vertices):
        self.vertices = list()
        self.labels = set()
        self.var = set()
        self.add_vertices(vertices)
        self.simple_partial_paths = {}
        self.visited_from_data_set = []

    def add_vertices(self, new_vertices):
        for vert in new_vertices:
            self.add_vertice(vert)

    def add_vertice(self, new_vertice):
        self.vertices += [new_vertice]
        self.labels.add(new_vertice.label)
        self.var |= new_vertice.defv | new_vertice.refv

    def __repr__(self):
        res = ""
        for vert in self.vertices:
            res += str(vert.label) + "\n"
            for n_e in vert.next_edges:
                res += str(n_e.__dict__) + "\n"
            res += "\n"

        return res

    def path(self, variables):
        visited = []
        current_vertice = self.vertices[0]  # First vertice
        visited += [current_vertice.label]
        while current_vertice.label != "exit":
            #print(current_vertice.label)
            next_edge = list(filter(lambda n_e: n_e.condition.evaluate(variables), current_vertice.next_edges))[0]
            variables = next_edge.command.execute(variables)
            current_vertice = list(filter(lambda vert: vert.label == next_edge.next_label, self.vertices))[0]
            visited += [current_vertice.label]
        return visited

    def add_simple_partial_paths(self, couple, path):
        #couple is a tuple (u,v)
        #path is a list of set
        self.simple_partial_paths[couple] = path

    def coverage_criteria(self, T):
        """It calculates the ratio between the number of vertices visited and the number total
        of vertices"""
        #T is a dataset 
        #print(T)
        variables_init = T
        for variables in T:
            #print(variables)
            variable1=dict(variables)
            p = self.path(variable1)
            #print(p)
            for elt in p:
                if elt not in self.visited_from_data_set:
                    self.visited_from_data_set.append(elt)
        
        nb_vertices = len(self.vertices)
        if nb_vertices != 0:
            vertices_label = [x.label for x in self.vertices]
            print("Coverage : {}".format(len(self.visited_from_data_set)/nb_vertices ))
            print("Vertices of the graph: {}".format(str(vertices_label)))
            print("Vertices visited : {}".format(str(self.visited_from_data_set)))
        else:
            raise ValueError("No vertices in this data set")



class Vertice:
    def __init__(self, label, next_edges=list()):
        self.label = label
        self.next_edges = list()
        if next_edges:
            self.add_next_edges(next_edges)
        self.defv = set()
        self.refv = set()

    def add_next_edges(self, new_edges):
        for edge in new_edges:
            self.add_next_edge(edge)

    def add_next_edge(self, new_edge):
        self.next_edges += [new_edge]
        if new_edge.command.type == "assign":
            self.defv.add(re.findall(r'[a-zA-Z]+', new_edge.command.representation)[0])
            self.refv |= set(re.findall(r'[a-zA-Z]+', new_edge.command.representation)[1:])
        self.refv |= set(re.findall(r'[a-zA-Z]+', new_edge.condition.representation))
        self.refv -= set(["true", "false", "not"])


class Edge:
    def __init__(self, B_expression, C_expression, next_label):
        self.condition = B_expression
        self.command = C_expression
        self.next_label = next_label


def apply_path(CG, variables):
    return CG.path(variables), variables


def find_vertice_with_label(CG, label):
    for vert in CG.vertices:
        if vert.label == label:
            return vert
    return None


if __name__ == '__main__':
    pass
