#Criteria 3
import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, Graph

def all_4_paths(CG,L,T):
    """The arguments are a control graph (CG), the list of paths that should 
    be visited to validate the criteria (L),and a data set of variables(T). It 
    checks if the criteria all_decisions is validated."""
    to_visit = list(L)
    not_visited = list(L)
    for t in T:
        p = apply_path(CG,t)[0]
        if p in not_visited:
            not_visited.remove(p)
    
    Graph.coverage_criteria2(to_visit, "not_visited", not_visited)
    if not_visited:
        print('test failed')
        return False
    else:
        print('test passed')
        return True

def all_4_paths_passed(CG):
    T = [
        {"X": -1},
        {"X": 2},
        {"X": -2}
    ]
    L = [
        [1, 2, 4, 5, "exit"], 
        [1, 3, 4, 5, "exit"], 
        [1, 2, 4, 6, "exit"], 
        [1, 3, 4, 6, "exit"]
        ]

    all_4_paths(CG, L, T)

def all_4_paths_failed(CG):
    T = [{"X": 2}
    ]
    L = [
        [1, 2, 4, 5, "exit"], 
        [1, 3, 4, 5, "exit"], 
        [1, 2, 4, 6, "exit"], 
        [1, 3, 4, 6, "exit"]
        ] 

    all_4_paths(CG, L, T)

if __name__=="__main__":
    print("Criteria 2 - all 4 paths")
    print("Control Graph is CG_Project_Example")
    print("\n")
    CG1 = CG_Project_Example()
    CG2 = CG_Project_Example()
    all_4_paths_passed(CG1)
    print("\n")
    all_4_paths_failed(CG2)