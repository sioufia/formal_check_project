#Criteria n°4
#We will take i = 1

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from control_graph import apply_path2

def test_path(T, apply_path):
    #L:list of the paths ; T: data set ; apply_path is a path for a specific prog
    print(T)
    L = [[1,2,3,1,"exit"], [1,2,4,1,"exit"]]
    to_visit = list(L)
    for t in T:
        p = apply_path(t)
        print(p)
        if p in to_visit:
            to_visit.remove(p)
    if to_visit:
        print('test failed')
    else:
        print('test passed')



def all_i_loop_passed():

    T = [
        {'X':10,'Y':5},
        {'X':5,'Y':10}
        ]
    
    apply_path = apply_path2

    test_path(T, apply_path)

def all_i_loop_failed():
    #It fails for i = 1 if X is always the douple of Y
    T = [
        {'X':30,'Y':15},
        {'X':10,'Y':5},
        {'X':20,'Y':10},

        ]
    
    apply_path = apply_path2

    test_path(T, apply_path)


all_i_loop_passed()
all_i_loop_failed()

    
