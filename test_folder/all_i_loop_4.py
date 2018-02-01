#Criteria n°4
#We will take i = 1

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_PGCD import CG_PGCD
from control_graph import apply_path

def all_i_loop(CG, L, T):
    #L:list of the paths ; T: data set ; apply_path is a path for a specific prog
    to_visit = L
    for t in T:
        p = apply_path(CG, t)[0]
        if p in to_visit:
            to_visit.remove(p)
    if to_visit:
        print('test failed')
    else:
        print('test passed')
        CG.coverage_criteria(T)



def all_i_loop_passed(CG):

    T = [
        {'X':10,'Y':5},
        {'X':5,'Y':10}
        ]
    
    L = [[1,2,3,1,"exit"], [1,2,4,1,"exit"]]

    all_i_loop(CG, L, T)

def all_i_loop_failed(CG):
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
    
