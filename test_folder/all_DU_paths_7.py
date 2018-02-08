#Criteria 7

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from itertools import product
from Control_Graphs.CG_Project_Example import CG_Project_Example
from Control_Graphs.CG_Dumb_loop_simple import CG_dumb_loop_simple
from control_graph import apply_path, find_vertice_with_label, Graph

def all_DU_paths(CG, T):
    """The arguments are a control graph (CG), and a data set of variables(T). 
    The list of elements named path_to_visit is a list of simple partial path 
    where there is a definition vertice and reference vertice of a variable 
    without redefinition between both vertices. This test checks if each path
    is visited at least once.
    It checks if the criteria all_DU_paths is validated."""
    path_to_visit = []
    path_not_visited = []
    for var in CG.var:
        vert_var_in_defv=set()
        vert_var_in_refv=set()
        for vert in CG.vertices:
            if var in vert.defv:
                vert_var_in_defv.add(vert.label)
            elif var in vert.refv:
                vert_var_in_refv.add(vert.label)
        couples = product(vert_var_in_defv, vert_var_in_refv)
        for vert_def, vert_ref in couples:
            #paths_remaining = list(CG.simple_partial_paths[(vert_def, vert_ref)])
            path_to_visit += list(CG.simple_partial_paths[(vert_def, vert_ref)])
            path_not_visited += list(CG.simple_partial_paths[(vert_def, vert_ref)])
            for t in T:
                path, variables = apply_path(CG, t)
                vert_found = False
                for label in path:
                    cur_vertice=find_vertice_with_label(CG,label)
                    if vert_def == label:
                        vert_found = True

                    elif vert_ref == label and vert_found:
                        if path in path_not_visited:
                            path_not_visited.remove(path)
                        break

                    elif vert_ref != label and var in cur_vertice.refv:
                        break
                        #print('Test failed')
                        #print(paths_remaining, var,vert_def, vert_ref, path)
                        #return False

        #if paths_remaining:
        #    print('Test failed')
        #    print(paths_remaining, var, vert_def, vert_ref, path)
        #    return False

    Graph.coverage_criteria2(path_to_visit, "not_visited", path_not_visited)
    if path_not_visited:
        print('Test failed')
    
    else:
        print('Test passed')
        return True

def all_DU_paths_passed(CG):
    T=[
        {'X':1},
        {'X':2},
        {'X':3}
    ]

    all_DU_paths(CG, T)

def all_DU_paths_failed(CG):
    T = [{'X':1}
    ]

    all_DU_paths(CG, T)

if  __name__=="__main__":
    print("Criteria 7 - all DU paths")
    print("Control Graph is CG_Project_Example")
    print("\n")
    CG1=CG_dumb_loop_simple()
    CG2=CG_dumb_loop_simple()
    all_DU_paths_passed(CG1)
    print("\n")
    all_DU_paths_failed(CG2)
