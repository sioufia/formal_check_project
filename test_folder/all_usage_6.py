import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label

def all_usages(CG,T):


    for var in CG.var:
        vert_var_in_defv=set()
        vert_var_in_refv=set()
        for vert in CG.vertices:
            if var in vert.defs:
    for t in T:
        path,variables=apply_path(CG,t)
        for var in variables:
            var_defined=False
            for label in path:
                cur_vertice=find_vertice_with_label(CG,label)
                if var in cur_vertice.defv:
                    var_defined=True
                    continue
                if var in cur_vertice.refv and var_defined:
                    variables_not_used.remove(var)
                    break
    if variables_not_used:
        print('Test failed')
        return False
    else:
        print('Test passed')
        return True
"""

if  __name__=="__main__":
    CG=CG_Project_Example()
    T=[
        {'X':1}
    ]
    all_definitions(CG,T)