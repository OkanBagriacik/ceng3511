import sys
from queue import Queue, PriorityQueue

total = len(sys.argv)
cmdags = str(sys.argv)

path = open(sys.argv[1])

graphSet = path.readlines()

path.close()

graph  = {}
nodeNumb = 0
nodePoint = ''

for line in graphSet:
    i = 0
    pointList = []
    graph.setdefault(line[0], '')
    
    for ch in line:

        #dugumlere ulas
        if i%5 == 0 and i != 0:
            
            i += 1

            #dugum yollarını sapta
            point = int(ch)

            if point > 0:
                
                pointList.append(line[i-3])
               
        else:
                i += 1

        graph[line[0]] = pointList

start = input("Please enter the start state: ")
goal = input("Please enter the goal state: ")

#BFS algorithm
def BFS(graph, start, goal):
    
    V = []
    Q = [[start]]

    while Q:
        connect = Q.pop(0)
        node = connect[-1]

        if start == goal:
            return connect
        elif node not in V:
            neighbour = graph[node]
            for element in neighbour:
                newCon = list(connect)
                newCon.append(element)
                Q.append(newCon)

                if element == goal:
                    return newCon

            V.append(node)

    return "no way"
        
#DFS algorithm

path = []
visited = []


def DFS(start, end, graph):

    path.append(start)
    visited.append(start)

    return DFS_findPath(start, end, graph)

def DFS_findPath(start, end, graph):
    for node in graph[path[len(path) - 1]]:
        if node not in visited:
            visited.append(node)
        else:
            continue

        path.append(node)

        if node == end:
            return path

        return DFS_findPath(start, end, graph)

#UCS algorithm

def UCS(graph, start, goal, path=[]):
        path = path + [start]
        if start == goal:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = UCS(graph, node, goal, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

#BFS print
BFSresult = BFS(graph, start, goal)

BFSelement = ""

for node in BFSresult:
    if node == BFSresult[-1]:
        BFSelement += node
    else:
        BFSelement += node + "-"

#DFS print

DFSresult = DFS(start, goal, graph)

DFSelement = ""

for node in DFSresult:
    if node == BFSresult[-1]:
        DFSelement += node
    else:
        DFSelement += node + "-"
    
#UCS print

UCSresult = UCS(graph, start, goal)

UCSelement = ""

for node in UCSresult:
    if node == UCSresult[-1]:
        UCSelement += str(node)
    else:
        UCSelement += str(node) + str(" - ")
    
UCSelement = UCSelement.replace('[', '')
UCSelement = UCSelement.replace(']', '')
UCSelement = UCSelement.replace("'", "")

print("BFS: ", BFSelement)
print("DFS: ", DFSelement)
print("UCS: ", UCSelement)

#print("BFS: ", BFS(graph, start, goal) )
#print("DFS: ", DFS(start, goal, graph) )
#print("UCS: ",  graph, start, goal) )
