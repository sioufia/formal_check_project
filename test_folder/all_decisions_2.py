#Criteria 2

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label, Graph

def all_decisions(CG,L,T):
    """The arguments are a control graph (CG), the list of edges that should 
    be visited to validate the criteria (L),and a data set of variables(T). It 
    checks if the criteria all_decisions is validated."""
    to_visit = list(L)
    visited = set()
    for t in T:
        path_visited = apply_path(CG,t)[0]
        edge_visited = set((path_visited[i], path_visited[i + 1]) for i in range(len(path_visited) - 1))
        visited |= edge_visited
    Graph.coverage_criteria2(to_visit, "visited" ,visited.intersection(to_visit))
    if L - visited:
        print('test failed')
    else:
        print('test passed')

def all_decisions_passed(CG):
    T = [
        {"X": -1},
        {"X": 2}
    ]
    L = {(2, 4), (3, 4), (5, "exit"), (6, "exit")}

    all_decisions(CG, L, T)

def all_decisions_failed(CG):
    T = [{'X':2}
    ]
    L = {(2, 4), (3, 4), (5, "exit"), (6, "exit")} 

    all_decisions(CG, L, T)

if __name__=="__main__":
    print("Criteria 2 - all decisions")
    print("Control Graph is CG_Project_Example")
    print("\n")
    CG1 = CG_Project_Example()
    CG2 = CG_Project_Example()
    all_decisions_passed(CG1)
    print("\n")
    all_decisions_failed(CG2)
    




