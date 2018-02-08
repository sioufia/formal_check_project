#Criteria 6

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from itertools import product

from Control_Graphs.CG_Project_Example import CG_Project_Example
from Control_Graphs.CG_Dumb import CG_Dumb
from control_graph import apply_path, find_vertice_with_label, Graph

def all_usages(CG,T):
    """The arguments are a control graph (CG), and a data set of variables(T). 
    The list of elements named couples_to_visit is a list of tuple (def,ref) with 
    def a vertice with assignement of a variable and ref a vertice with a 
    reference of this variable . This test checks if each tuple are visited without
    a redefinition between both.
    It checks if the criteria all_usages is validated."""
    couples_to_visit = []
    couples_not_visited = []
    for var in CG.var:
        vert_var_in_defv=set()
        vert_var_in_refv=set()
        for vert in CG.vertices:
            if var in vert.defv:
                vert_var_in_defv.add(vert.label)
            elif var in vert.refv:
                vert_var_in_refv.add(vert.label)
        #print(vert_var_in_defv)
        #print(vert_var_in_refv)
        couples = product(vert_var_in_defv, vert_var_in_refv)
        couples_to_visit += couples
        couples_not_visited += couples
        print(couples_to_visit)
        for t in T:
            path,variables=apply_path(CG,t)
            for vert_def, vert_ref in couples:
                vert_def_found = False
                for vert in path:
                    if vert_def == vert.label:
                        vert_found = True

                    elif vert_ref == vert.label and vert_found:
                        couples_not_visited.remove((vert_def, vert_ref))
                        break
                    
                    elif vert_ref != vert.label and var in vert.refv:
                        break
                        #print('Test failed')
                        #return False
        
        #if couples_not_visited:
            #print('Test failed')
            #print(couples_remaining, var)
            #return False

    Graph.coverage_criteria2(couples_to_visit, "not_visited", couples_not_visited)
    if couples_not_visited:
        print('Test failed')
        return False

    else:
        print('Test passed')
        return True

def all_usages_passed(CG):
    T=[
        {'X':100, 'Y':5},
        {'X':5, 'Y':100}
    ]

    all_usages(CG, T)

def all_usages_failed(CG):
    T=[
        {'X':1},
        {'X':-1},
        {'X':-10}
    ]

    all_usages(CG, T)

if  __name__=="__main__":
    print("Criteria 6 - all usage")
    print("\n")
    print("Control Graph is CG_Project_Example")
    CG1=CG_Project_Example()
    all_usages_failed(CG1)
    
    print("Control Graph is CG_Dumb")
    CG2=CG_Dumb()
    all_usages_passed(CG2)

