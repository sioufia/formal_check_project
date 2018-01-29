import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from itertools import product
from Control_Graphs.CG_Project_Example import CG_Project_Example
from Control_Graphs.CG_Dumb_loop_simple import CG_dumb_loop_simple
from control_graph import apply_path, find_vertice_with_label

def all_DU_paths(CG, T):
    for var in CG.var:
        vert_var_in_defv=set()
        vert_var_in_refv=set()
        for vert in CG.vertices:
            if var in vert.defv:
                vert_var_in_defv.add(vert.label)
            elif var in vert.refv:
                vert_var_in_refv.add(vert.label)
        couples = product(vert_var_in_defv, vert_var_in_refv)
        paths_remaining=list(CG.simple_partial_paths[(vert_def,vert_ref)] for (vert_def,vert_ref) in couples)
        for t in T:
            path, variables = apply_path(CG, t)
            for vert_def, vert_ref in couples:
                vert_found = False
                for vert in path:
                    if vert_def == vert.label:
                        vert_found = True

                    elif vert_ref == vert.label and vert_found:
                        paths_remaining.remove(path)
                        break

                    elif vert_ref != vert.label and var in vert.refv:
                        print('Test failed')
                        return False

        if paths_remaining:
            print('Test failed')
            print(paths_remaining, var)
            return False

    print('Test passed')
    return True

if  __name__=="__main__":
    CG=CG_dumb_loop_simple()
    T=[
        {'X':1},
    ]
    print('Dumb Loop Simple')
    all_DU_paths(CG, T)