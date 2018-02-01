import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label

def all_decisions(CG,L,T):
    to_visit = list(L)
    visited = set()
    for t in T:
        path_visited = apply_path(CG,t)[0]
        edge_visited = set((path_visited[i], path_visited[i + 1]) for i in range(len(path_visited) - 1))
        visited |= edge_visited
    if L - visited:
        print('test failed')
    else:
        print('test passed')
        CG.coverage_criteria(T)


if __name__=="__main__":
    Control_Graph = CG_Project_Example()
    L = {(2, 4), (3, 4), (5, "exit"), (6, "exit")}
    T = [
        {"X": -1},
        {"X": 2}
    ]
    all_decisions(Control_Graph,L,T)




