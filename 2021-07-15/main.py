from random import randint
import threading


#Functions
def runStart(maze, start, end, result):
    if (start == end):
        for i in range(len(maze)):
            print(maze[i])
        print("Path found: ", result, " steps")

    runLeft(maze, start, end, result)
    runRight(maze, start, end, result)
    runUp(maze, start, end, result)
    runDown(maze, start, end, result)

def runLeft(maze, start, end, result):

    path = maze
    left = (start[1] - 1)

    if not ( (left < 0) or (path[start[0]][left]) ):
        path[start[0]][start[1]] = '<'
        start = (start[0], left)
        runStart(path, start, end, result + 1)

def runRight(maze, start, end, result):

    path = maze
    right = (start[1] + 1)

    if not ( (right > len(path) - 1) or (path[start[0]][right]) ):
        path[start[0]][start[1]] = '>'
        start = (start[0], right)
        runStart(path, start, end, result + 1)

def runUp(maze, start, end, result):

    path = maze
    up = (start[0] - 1)

    if not ( (up < 0) or (path[up][start[1]]) ):
        path[start[0]][start[1]] = '^'
        start = (up, start[1])
        runStart(path, start, end, result + 1)

def runDown(maze, start, end, result):

    path = maze
    down = (start[0] + 1)

    if not ( (down > len(path) - 1) or (path[down][start[1]]) ):
        path[start[0]][start[1]] = 'v'
        start = (down, start[1])
        runStart(path, start, end, result + 1)

# Classes
class runner(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        runStart(maze, start, end, result)

#Input
#rows = input(int("M (rows):"))
#cols = input(int("N (columns):"))
rows = 6
cols = 6

#maze = [[(randint(0,1)) for j in range(cols)] for i in range(rows)]
maze = [[0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

#start = input("Starting point (x, y):")
#end = input("Ending point (x, y):")
start = (3, 0)
end = (0, 0)

maze[start[0]][start[1]] = 0
maze[end[0]][end[1]] = 0

result = 0

#Run







#Output
"""""
print("Maze:")
for i in range(len(maze)):
    print(maze[i])

print("")
"""
runStart(maze, start, end, result)
#print("Shortest path found: ")