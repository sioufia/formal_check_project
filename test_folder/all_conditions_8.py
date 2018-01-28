#Criteria 8
# We need to test 2 paths : one for which all the conditions are True and another for which all the conditions are wrong

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from control_graph import apply_path

def test_path(L, T, apply_path):
    #L:list of the paths ; T: data set ; apply_path is a path for a specific prog
    to_visit = list(L)
    for t in T:
        p = apply_path(t)
        if p in to_visit:
            to_visit.remove(p)
    if to_visit:
        print('test failed')
    else:
        print('test passed')



def all_conditions_passed():

    T = [
        {'X':-1},
        {'X':10}
        ]
    
    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    test_path(L, T, apply_path)

def all_conditions_failed():
    #A requirement to pass the test is to have X=-1 as initial value
    T = [
        {'X':-5}
        ]

    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    test_path(L, T, apply_path)


all_conditions_passed()
all_conditions_failed()

    
