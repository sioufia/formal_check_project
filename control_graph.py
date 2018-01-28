from boolean_exp import Boolean_Exp
from command_exp import Command_Exp
import re

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.labels=set([vert.label for vert in vertices])

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

    def path(self,variables):
        visited=[]
        current_vertice=self.vertices[0] # First vertice
        visited+=[current_vertice.label]
        while current_vertice.label!="exit":
            next_edge=list(filter(lambda n_e:n_e.cond.evaluate(variables), current_vertice.next_edges))[0]
            variables=next_edge.com.execute(variables)
            current_vertice=list(filter(lambda vert:vert.label==next_edge.next_label, self.vertices))[0]
            visited += [current_vertice.label]
        return visited

class Vertice:
    def __init__(self, label, next_edges=list()):
        self.label = label
        self.next_edges = list(next_edges)
        self.defv = []
        self.refv = []

    def add_next_edges(self, new_edges):
        self.next_edges += new_edges

    def add_next_edge(self, new_edge):
        self.next_edges += [new_edge]
        if new_edge.com.type == "assign":
            self.defv.append({new_edge.com.representation.split(":=")[0]})
        if new_edge.com.type == "skip":
            pass


class Edge:
    def __init__(self, B_expression, C_expression, next_label):
        self.cond = B_expression
        self.com = C_expression
        self.next_label = next_label

def apply_path(CG, variables):
    return CG.path(variables), variables

if __name__=='__main__':
    pass
