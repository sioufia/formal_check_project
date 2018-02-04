#Criteria 8
# We need to test 2 paths : one for which all the conditions are True and another for which all the conditions are wrong

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label, Graph

def all_conditions(CG, L, T):
    #L:list of the paths ; T: data set ; apply_path is a path for a specific prog
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
        #CG.coverage_criteria(T)



def all_conditions_passed(CG):

    T = [
        {'X':-1},
        {'X':10}
        ]
    
    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    all_conditions(CG, L, T)

def all_conditions_failed(CG):
    #A requirement to pass the test is to have X=-1 as initial value
    T = [
        {'X':-5}
        ]

    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    all_conditions(CG, L, T)

if __name__=="__main__":
    Control_Graph1 = CG_Project_Example()
    Control_Graph2 = CG_Project_Example()  
    all_conditions_passed(Control_Graph1)
    all_conditions_failed(Control_Graph2)

    
