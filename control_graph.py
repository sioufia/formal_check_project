"""File that enables the construction of Control Graph from a WHILE program"""
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
        """Functions that gives the path took by the program for a specific variable"""
        new_variables=dict(variables)
        visited = []
        current_vertice = self.vertices[0]  # First vertice
        visited += [current_vertice.label]
        while current_vertice.label != "exit":
            next_edge = list(filter(lambda n_e: n_e.condition.evaluate(new_variables), current_vertice.next_edges))[0]
            new_variables = next_edge.command.execute(new_variables)
            current_vertice = list(filter(lambda vert: vert.label == next_edge.next_label, self.vertices))[0]
            visited += [current_vertice.label]
        return visited, new_variables

    def add_simple_partial_paths(self, couple, path):
        #couple is a tuple (u,v)
        #path is a list of set
        self.simple_partial_paths[couple] = path

    @staticmethod
    def coverage_criteria2(to_visit, type_numerator, numerator):
        """It calculates the ratio between the elements that have been visited and the all the elements of the criteria
        that should be visited
        - to_visit is a list of the elements that covers the criteria
        - not_visited is a list of the elements from to_visit that have not been visited
        """
        if to_visit:
            print("to_visit : {} ".format(to_visit))
            if type_numerator == "not_visited":
                print("not_visited : {} ".format(numerator))
                print ("Coverage criteria : {}".format(1 - (len(numerator) / len(to_visit)) ))
            elif type_numerator == "visited":
                print("visited : {} ".format(numerator))
                print ("Coverage criteria : {}".format(len(numerator) / len(to_visit)))

        else:
            raise ValueError('to_visit is empty')



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
    """It returns the path of control graph for specific variables"""
    return CG.path(variables)


def find_vertice_with_label(CG, label):
    for vert in CG.vertices:
        if vert.label == label:
            return vert
    return None


if __name__ == '__main__':
    pass
