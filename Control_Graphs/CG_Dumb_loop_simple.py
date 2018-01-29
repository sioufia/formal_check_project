from control_graph import Graph, Vertice, Edge, apply_path
from boolean_exp import Boolean_Exp
from command_exp import Command_Exp

def CG_dumb_loop_simple():
    "Create a graphe with simple intermediary loop for question 7"
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True = Boolean_Exp(lambda x: True, "true")
    
    V1 = Vertice(1)
    def func1(variables):
        variables['Y'] = 1
        return variables
    C1 = Command_Exp(func1, "Y:=1", type="assign")
    V1.add_next_edge(Edge(B_True, C1, 2))

    V2 = Vertice(2)
    B2_1 = Boolean_Exp(lambda vars:vars['X']==1,"X=1")
    V2.add_next_edge(Edge(B2_1, C_skip, 4))
    B2_2 = Boolean_Exp(lambda vars:vars['X']!=1,"X!=1")
    V2.add_next_edge(Edge(B2_1, C_skip, 2))

    V3 = Vertice(3)
    def func2(variables):
        variables['X'] = variables['X'] - 1
        return variables
    C3 = Command_Exp(func2 , "X:=1", type="assign")
    V3.add_next_edge(Edge(B_True, C3, 2))

    V4 = Vertice(4)
    def func4(variables):
        variables['X'] = variables['Y']
        return variables
    C4 = Command_Exp(func4 , "X:=Y", type="assign")
    V4.add_next_edge(Edge(B_True, C4, "exit"))

    Vexit = Vertice("exit")
    Control_Graph = Graph([V1,V2,V3,Vexit])
    Control_Graph.add_simple_partial_paths((V1.label,V4.label),[{1,2,4},{1,2,3,2,4}])
    return Control_Graph

    if __name__ == "__main__":
        CG = CG_dump_loop_simple()
        print(CG.__dict__)
        for vert in CG.vertices:
            print(vert.__dict__)


