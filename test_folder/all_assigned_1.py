#Criteria n° 1
import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label, Graph


def all_assigned(CG,L,T):
    to_visit = L
    not_visited = list(L)
    for t in T:
        p = apply_path(CG,t)
        for label in p[0]:
            if label in not_visited:
                not_visited.remove(label)
    
    Graph.coverage_criteria2(to_visit, "not_visited", not_visited)
    if not_visited:
        print('test failed')
        return False
    else:
        print('test passed')
        #CG.coverage_criteria(T)
        return True
        

if __name__=="__main__":
    Control_Graph = CG_Project_Example()
    L = [2,3,5,6]
    T = [
    {'X':-1}, 
    {'X':1}, 
    {'X':-1} 
    ]
    all_assigned(Control_Graph, L, T)

