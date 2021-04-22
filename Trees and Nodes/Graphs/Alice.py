import sys
# Class Definitions


class Node:
    def __init__(self, n: str):
        self.name = n
        self.neighbors = set()

    def addNeighbor(self, v: str):
        if v not in self.neighbors:
            self.neighbors.add(v)


class Maze:
    def __init__(self):
        self.nodes = {}
        self.size = 0
        self.edgesize = 0
        self.start = None
        self.goal = None

    def addNode(self, node: Node):
        if node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        return False

    def reset(self):
        for v in self.nodes:
            self.nodes[v].totalDistance = float('inf')
            self.nodes[v].prevNode = None

    def addPath(self, n: str, dist: str):
        name = eval(n)  # list of coords
        offset = eval(dist)  # list of coords
        neighbor = str([a+b for a, b in zip(name, offset)]).replace(' ', '')
        if n in self.nodes and neighbor in self.nodes:
            self.nodes[n].addNeighbor(neighbor)
            self.edgesize += 1
            return True
        return False

    def printGraph(self):
        for key in sorted(list(self.nodes.keys())):
            print(key + ":" + str(self.nodes[key].neighbors))

    def BFShortestPath(self):
        colour = {}
        d = {}
        pi = {}

        for v in self.nodes:
            d[v] = float('inf')
            pi[v] = None
        startingPoint = makeStart(self.start)
        d[startingPoint] = 0
        Q = [startingPoint]
        while len(Q) > 0:
            u = Q.pop()
            for v in self.nodes[u].neighbors:
                if d[v] == float('inf'):
                    d[v] = d[u]+1
                    pi[v] = u
                    Q.insert(0, v)
        # Find the path
        goalDists = [d[makeGoal(self.goal, i)] for i in range(1, n)]
        bestDepth = goalDists.index(min(goalDists))+1
        path = [makeGoal(self.goal, bestDepth)]
        while (pi[path[-1]] != None):
            path.append(pi[path[-1]])
        path.reverse()

        if path[0] == startingPoint:
            return path

# Make all the node names for the n*n*n-1 representation of the maze


def makeNodeNames(n):
    nodeList = [[[str([i, j, k]).replace(' ', '')
                  for j in range(n)]
                 for i in range(n)]
                for k in range(1, n)]
    return nodeList

# Add nodes with the above node names to the Maze


def addNodesToMaze(maze: Maze, nodeList: list):
    for plane in nodeList:
        for row in plane:
            for n in row:
                maze.addNode(Node(n))

# Generate offset vectors based on node values


def makeOffsets(n: str, nodeInfo: str):
    if nodeInfo[0] == "GOAL":
        return []
    nlist = eval(n)
    stepsize = nlist[2]+colours[nodeInfo[0]]
    offsets = []
    for arrowstring in nodeInfo[1:]:
        offset = 3*[0]
        offset[0] = stepsize*directions[arrowstring][0]
        offset[1] = stepsize*directions[arrowstring][1]
        offset[2] = colours[nodeInfo[0]]
        offsets.append(str(offset).replace(' ', ''))
    return offsets

# Name of the starting node


def makeStart(strtup):
    tup = eval(strtup)
    start = 3*[1]
    start[0] = tup[0]
    start[1] = tup[1]
    return str(start).replace(' ', '')

# Name of the goal node with a stepsize of i


def makeGoal(strtup, i):
    tup = eval(strtup)
    goal = 3*[i]
    goal[0] = tup[0]
    goal[1] = tup[1]
    return str(goal).replace(' ', '')


txtfileName = sys.argv[1]

# txt to maze Translation

# Import and format txt file
f = open(sys.path[0]+"\\"+txtfileName, "r")
lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
f.close()
n = eval(lines[0])

# Make a maze with all the nodes (they aren't connected by edges yet)
myMaze = Maze()
names = makeNodeNames(n)
addNodesToMaze(myMaze, names)

# Make start and goal
myMaze.size = n
myMaze.start = lines[1]
myMaze.goal = lines[2]

# define translations
directions = {'up': (-1, 0),
              'upright': (-1, 1),
              'right': (0, 1),
              'downright': (1, 1),
              'down': (1, 0),
              'downleft': (1, -1),
              'left': (0, -1),
              'upleft': (-1, -1)}
colours = {'red': 1, 'black': 0, 'yellow': -1}

# Make Edges
for planeIndex in range(1, n):
    for rowIndex in range(len(lines[4:])):
        rowArrows = lines[rowIndex+4].split(';')
        for nodeIndex in range(len(rowArrows)):
            curNode = str([rowIndex, nodeIndex, planeIndex]).replace(' ', '')
            nodeInfo = rowArrows[nodeIndex].replace(' ', '').split(',')
            offsets = makeOffsets(curNode, nodeInfo)
            for offset in offsets:
                myMaze.addPath(curNode, offset)
# myMaze.printGraph()

# PathFinding
unformattedPath = myMaze.BFShortestPath()

if unformattedPath:  # If a path is found
    # remove stepsize dimension
    formattedPath = [eval(step)[:2] for step in unformattedPath]
    print("\nShortest Path\n"+str(formattedPath)+'\n')
    print('Shortest Path Length\n'+str(len(formattedPath)-1))

else:
    print("No solution found :(")
