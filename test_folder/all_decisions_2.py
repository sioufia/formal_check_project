import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from control_graph import apply_path

L = {(2, 4), (3, 4), (5, "exit"), (6, "exit")}

T = [
    {"X": -1},
    {"X": 2}
]

visited = set()
for t in T:
    path_visited = apply_path(t)
    edge_visited = set((path_visited[i], path_visited[i + 1]) for i in range(len(path_visited) - 1))
    visited |= edge_visited

if L - visited:
    print('test failed')
else:
    print('test passed')
