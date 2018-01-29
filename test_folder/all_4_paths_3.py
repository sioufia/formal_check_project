import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path

def test(CG,L,T):
    to_visit = list(L)
    for t in T:
        p = apply_path(CG,t)
        if p in to_visit:
            to_visit.remove(p)
    if to_visit:
        print('test failed')
        return False
    else:
        print('test passed')
        return True

if __name__=="__main__":
    Control_Graph = CG_Project_Example()
    L = [[1, 2, 4, 5, "exit"], [1, 3, 4, 5, "exit"], [1, 2, 4, 6, "exit"], [1, 3, 4, 6, "exit"]]
    T = [
        {"X": -1},
        {"X": 2},
        {"X": -2}
    ]
    test(Control_Graph,L,T)