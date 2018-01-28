from boolean_exp import Boolean_Exp
from command_exp import Command_Exp

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

    def add_next_edges(self, new_edges):
        self.next_edges += new_edges

    def add_next_edge(self, new_edge):
        self.next_edges += [new_edge]


class Edge:
    def __init__(self, B_expression, C_expression, next_label):
        self.cond = B_expression
        self.com = C_expression
        self.next_label = next_label



def control_graph_1():
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True=Boolean_Exp(lambda x: True, "true")
    V1 = Vertice(1)
    B1=Boolean_Exp(lambda vars:vars['X']<=0,"X<=0")

    V1.add_next_edge(Edge(B1, C_skip, 2))
    B1_1=Boolean_Exp(lambda vars:vars['X']>0,"not(X<=0)")
    V1.add_next_edge(Edge(B1_1, C_skip, 3))

    V2=Vertice(2)
    def fun_2(variables):
        variables['X']*=-1
        return variables
    C2=Command_Exp(fun_2,"X:=-X",type="assign")
    V2.add_next_edge(Edge(B_True, C2, 4))

    V3=Vertice(3)
    def fun_3(variables):
        variables['X'] =1-variables['X']
        return variables
    C3=Command_Exp(fun_3,"X:=1-X", type="assign")
    V3.add_next_edge(Edge(B_True, C3, 4))

    V4 = Vertice(4)
    B4=Boolean_Exp(lambda vars: vars["X"]==1, "X=1")
    B4_1=Boolean_Exp(lambda vars: vars["X"]!=1, "not(X=1)")
    V4.add_next_edges([Edge(B4, C_skip, 5), Edge(B4_1, C_skip, 6)])

    V5 = Vertice(5)
    def fun_5(variables):
        variables['X'] =1
        return variables
    C5=Command_Exp(fun_5,"X:=1", type="assign")
    V5.add_next_edge(Edge(B_True, C5, "exit"))

    V6 = Vertice(6)
    def fun_6(variables):
        variables['X'] += 1
        return variables 
    C6 = Command_Exp(fun_6,"X:=X+1",type="assign")
    V6.add_next_edge(Edge(B_True, C6, "exit"))
    
    Vexit = Vertice("exit")
    Control_Graph = Graph([V1, V2, V3, V4, V5, V6, Vexit])
    return Control_Graph

def control_graph_2():
    C_skip = Command_Exp(lambda x: x, "skip", type="skip")
    B_True=Boolean_Exp(lambda x: True, "true")
    
    V1 = Vertice(1)
    B1 = Boolean_Exp(lambda vars:vars['X']!=vars['Y'], "X!=Y")
    V1.add_next_edge(Edge(B1, C_skip, 2))
    B1_1 = Boolean_Exp(lambda vars:vars['X']==vars['Y'], "X=Y")
    V1.add_next_edge(Edge(B1_1, C_skip, 'exit'))

    V2=Vertice(2)
    B2 = Boolean_Exp(lambda vars:vars['X']>vars['Y'], "X>Y")
    V2.add_next_edge(Edge(B2, C_skip, 3))
    B2_2 = Boolean_Exp(lambda vars:vars['X']<=vars['Y'], "X<=Y")
    V2.add_next_edge(Edge(B2_2, C_skip, 4))

    V3=Vertice(3)
    def fun_3(variables):
        variables['X'] = variables['X'] - variables['Y']
        return variables
    C3=Command_Exp(fun_3,"X=X-Y", type="assign")
    V3.add_next_edge(Edge(B_True,C3,1))

    V4=Vertice(4)
    def fun_4(variables):
        variables['Y'] = variables['Y'] - variables['X']
        return variables
    C4=Command_Exp(fun_4,"Y=Y-X", type="assign")
    V4.add_next_edge(Edge(B_True,C4,1))

    Vexit = Vertice("exit")
    Control_Graph = Graph([V1, V2, V3, V4, Vexit])
    return Control_Graph


def control_graph_3():
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


def apply_path(variables):
    CG=control_graph_2()
    return CG.path(variables), variables

if __name__=='__main__':
    CG=control_graph_2()
    Va = {'X':10, 'Y':3}
    print(CG.path(Va))
