import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from control_graph import apply_path

L = [[1,2,4,5,"exit"],[1,3,4,5,"exit"],[1,2,4,6,"exit"],[1,3,4,6,"exit"]]

T = [
    {"X": -1},
    {"X": 2},
    {"X": -2}
]

to_visit = list(L)
for t in T:
    p = apply_path(t)
    if p in to_visit:
        to_visit.remove(p)
if to_visit:
    print('test failed')
else:
    print('test passed')
