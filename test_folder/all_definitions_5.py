#Criteria 5

import sys

sys.path.insert(0, sys.path[0][:len(sys.path[0]) - 12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label, Graph


def all_definitions(CG, T):
    """The arguments are a control graph (CG), and a data set of variables(T). 
    The list of elements named vert_to_visit is the vertices where there is an 
    assignement of a variables. This test checks if there are used at least once.
    It checks if the criteria all_definitions is validated."""
    for var in CG.var:
        vert_var_in_defv = set()
        for vert in CG.vertices:
            if var in vert.defv:
                vert_var_in_defv.add(vert.label)
        vert_to_visit = set(vert_var_in_defv)
        vert_not_visited = set(vert_var_in_defv)

        for t in T:
            path, variables = apply_path(CG, t)
            for definition_vert in vert_var_in_defv:
                def_vert_visited = False
                for label in path:
                    cur_vertice = find_vertice_with_label(CG, label)
                    if label == definition_vert:
                        def_vert_visited = True
                        continue
                    if var in cur_vertice.refv and def_vert_visited:
                        vert_not_visited.remove(definition_vert)
                        break
                    
        Graph.coverage_criteria2(vert_to_visit, "not_visited", vert_not_visited)
        if vert_not_visited:
            print('Test failed')
            return False

    print('Test passed')

    return True

def all_definitions_passed(CG):
    T = [
    {'X':-1}, 
    {'X':1}, 
    ]

    all_definitions(CG, T)

def all_definitions_failed(CG):
    T = [{'X':1}
    ]

    all_definitions(CG, T)

if __name__ == "__main__":
    print("Criteria 5 - all definitions")
    print("Control Graph is CG_Project_Example")
    print("\n")
    CG1 = CG_Project_Example()
    CG2 = CG_Project_Example()
    all_definitions_passed(CG1)
    print("\n")
    all_definitions_failed(CG2)
