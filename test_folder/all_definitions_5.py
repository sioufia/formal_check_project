import sys

sys.path.insert(0, sys.path[0][:len(sys.path[0]) - 12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label


def all_definitions(CG, T):
    for var in CG.var:
        vert_var_in_defv = set()
        for vert in CG.vertices:
            if var in vert.defv:
                vert_var_in_defv.add(vert.label)
        vert_to_visit = set(vert_var_in_defv)

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
                        vert_to_visit.remove(definition_vert)
                        break
        if vert_to_visit:
            print('Test failed')
            return False

    print('Test passed')
    return True


if __name__ == "__main__":
    CG = CG_Project_Example()
    T = [
        {'X': 1},
        {'X':-1}
    ]
    all_definitions(CG, T)
