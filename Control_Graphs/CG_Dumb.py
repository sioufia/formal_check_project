"""File that creates the CG_dumb control graph"""

from control_graph import Graph, Vertice, Edge, apply_path
from boolean_exp import Boolean_Exp
from command_exp import Command_Exp


def CG_Dumb():
    """Control Graph of the dumb program"""
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True = Boolean_Exp(lambda x: True, "true")

    V1 = Vertice(1)

    def fun_1(variables):
        variables['X'] = 1
        return variables

    C1 = Command_Exp(fun_1, "X:=1",type="assign")
    V1.add_next_edge(Edge(B_True, C1, 2))

    V2 = Vertice(2)

    def fun_2(variables):
        variables['Y'] = variables['X'] + 1
        return variables

    C2 = Command_Exp(fun_2, "Y:=X+1",type="assign")
    V2.add_next_edge(Edge(B_True, C_skip, "exit"))

    Vexit = Vertice("exit")
    Control_Graph = Graph([V1, V2, Vexit])
    return Control_Graph


if __name__ == "__main__":
    CG = CG_Dumb()
    print(CG.__dict__)
    for vert in CG.vertices:
        print(vert.__dict__)
