#Criteria n° 1
import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])
from control_graph import apply_path

TA = set([2,3,5,6]) #List of the labels with assignements

X2 = {'X':-1} #For labels 2 and 6
X3 = {'X':1} #For labels 3 and 6
X5 = {'X':-1} #For label 5

visited = set([])
visited |= set(apply_path(X2))
visited |= set(apply_path(X3))
visited |= set(apply_path(X5))

if len(TA.difference(visited)) == 0:
    print("Test passed!")
else:
    print("Test not passed!")



