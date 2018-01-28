from control_graph import Graph, Vertice, Edge, Command_Exp, Boolean_Exp, apply_path


def CG_Project_Example():
    """Control Graph of the example given in th eproject description"""
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True = Boolean_Exp(lambda x: True, "true")

    V1 = Vertice(1)
    B1 = Boolean_Exp(lambda vars: vars['X'] <= 0, "X<=0")

    V1.add_next_edge(Edge(B1, C_skip, 2))
    B1_1 = Boolean_Exp(lambda vars: vars['X'] > 0, "not(X<=0)")
    V1.add_next_edge(Edge(B1_1, C_skip, 3))

    V2 = Vertice(2)

    def fun_2(variables):
        variables['X'] *= -1
        return variables

    C2 = Command_Exp(fun_2, "X:=-X", type="assign")
    V2.add_next_edge(Edge(B_True, C2, 4))


    V3 = Vertice(3)

    def fun_3(variables):
        variables['X'] = 1 - variables['X']
        return variables

    C3 = Command_Exp(fun_3, "X:=1-X", type="assign")
    V3.add_next_edge(Edge(B_True, C3, 4))

    V4 = Vertice(4)
    B4 = Boolean_Exp(lambda vars: vars["X"] == 1, "X=1")
    B4_1 = Boolean_Exp(lambda vars: vars["X"] != 1, "not(X=1)")
    V4.add_next_edges([Edge(B4, C_skip, 5), Edge(B4_1, C_skip, 6)])

    V5 = Vertice(5)

    def fun_5(variables):
        variables['X'] = 1
        return variables

    C5 = Command_Exp(fun_5, "X:=1", type="assign")
    V5.add_next_edge(Edge(B_True, C5, "exit"))

    V6 = Vertice(6)

    def fun_6(variables):
        variables['X'] += 1
        return variables

    C6 = Command_Exp(fun_6, "X:=X+1", type="assign")
    V6.add_next_edge(Edge(B_True, C6, "exit"))

    Vexit = Vertice("exit")

    Control_Graph = Graph([V1, V2, V3, V4, V5, V6, Vexit])

    return Control_Graph

if __name__=="__main__":
    CG=CG_Project_Example()
    variables={"X":2}
    print(apply_path(CG,variables))