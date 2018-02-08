#Criteria n°4
#We will take i = 1

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_PGCD import CG_PGCD
from control_graph import apply_path, Graph

def all_i_loop(CG, L, T):
    """The arguments are a control graph (CG), the list of paths that should 
    be visited to validate the criteria (L),and a data set of variables(T). It 
    checks if the criteria all_assigned is validated."""
    to_visit = list(L)
    not_visited = list(L)
    for t in T:
        p = apply_path(CG, t)[0]
        if p in not_visited:
            not_visited.remove(p)
    
    Graph.coverage_criteria2(to_visit, "not_visited", not_visited)
    if not_visited:
        print('test failed')
    else:
        print('test passed')



def all_i_loop_passed(CG):
    """A specific data set that validates the criteria"""

    T = [
        {'X':10,'Y':5},
        {'X':5,'Y':10}
        ]
    
    L = [[1,2,3,1,"exit"], [1,2,4,1,"exit"]]

    all_i_loop(CG, L, T)

def all_i_loop_failed(CG):
    """A specific data set that invalidates the criteria"""
    #It fails for i = 1 if X is always the douple of Y
    T = [
        {'X':30,'Y':15},
        {'X':10,'Y':5},
        {'X':20,'Y':10},

        ]
    
    L = [[1,2,3,1,"exit"], [1,2,4,1,"exit"]]

    all_i_loop(CG, L, T)
    

if  __name__=="__main__":
    CG1=CG_PGCD()
    CG2=CG_PGCD()
    all_i_loop_passed(CG1)
    all_i_loop_failed(CG2)
    
