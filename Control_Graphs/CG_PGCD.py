"""File that creates the CG_PGCD control graph"""

from control_graph import Graph, Vertice, Edge, Command_Exp, Boolean_Exp, apply_path


def CG_PGCD():
    """Control Graph of a program computing PGCD between two integers"""
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True = Boolean_Exp(lambda x: True, "true")

    V1 = Vertice(1)
    B1 = Boolean_Exp(lambda vars: vars['X'] != vars['Y'], "X!=Y")
    V1.add_next_edge(Edge(B1, C_skip, 2))
    B1_1 = Boolean_Exp(lambda vars: vars['X'] == vars['Y'], "X=Y")
    V1.add_next_edge(Edge(B1_1, C_skip, 'exit'))

    V2 = Vertice(2)
    B2 = Boolean_Exp(lambda vars: vars['X'] > vars['Y'], "X>Y")
    V2.add_next_edge(Edge(B2, C_skip, 3))
    B2_2 = Boolean_Exp(lambda vars: vars['X'] <= vars['Y'], "X<=Y")
    V2.add_next_edge(Edge(B2_2, C_skip, 4))

    V3 = Vertice(3)

    def fun_3(variables):
        variables['X'] = variables['X'] - variables['Y']
        return variables

    C3 = Command_Exp(fun_3, "X=X-Y", type="assign")
    V3.add_next_edge(Edge(B_True, C3, 1))

    V4 = Vertice(4)

    def fun_4(variables):
        variables['Y'] = variables['Y'] - variables['X']
        return variables

    C4 = Command_Exp(fun_4, "Y=Y-X", type="assign")
    V4.add_next_edge(Edge(B_True, C4, 1))

    Vexit = Vertice("exit")
    Control_Graph = Graph([V1, V2, V3, V4, Vexit])
    return Control_Graph

if __name__=="__main__":
    CG=CG_PGCD()
    variables={"X":12,"Y":16}
    print(apply_path(CG,variables))
    print(CG.__dict__)
    for vert in CG.vertices:
        print(vert.__dict__)
