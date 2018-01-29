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
        for vert_def, vert_ref in couples:
            paths_remaining = list(CG.simple_partial_paths[(vert_def, vert_ref)])
            for t in T:
                path, variables = apply_path(CG, t)
                vert_found = False
                for label in path:
                    cur_vertice=find_vertice_with_label(CG,label)
                    if vert_def == label:
                        vert_found = True

                    elif vert_ref == label and vert_found:
                        if path in paths_remaining:
                            paths_remaining.remove(path)
                        break

                    elif vert_ref != label and var in cur_vertice.refv:
                        print('Test failed')
                        print(paths_remaining, var,vert_def, vert_ref, path)
                        return False

        if paths_remaining:
            print('Test failed')
            print(paths_remaining, var, vert_def, vert_ref, path)
            return False



    print('Test passed')
    return True

if  __name__=="__main__":
    CG=CG_dumb_loop_simple()
    T=[
        {'X':1},
        {'X':2},
        {'X':3}
    ]
    print('Dumb Loop Simple')
    all_DU_paths(CG, T)