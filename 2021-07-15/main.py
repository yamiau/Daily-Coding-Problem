from random import randint
import threading

# Classes
class Runner(threading.Thread):
    def __init__(self, ID):
        threading.Thread.__init__(self)
        self.ID = ID

    def run(self, maze, start, end, steps):
        if (start == end):
            for i in range(len(maze)):
                print(maze[i])
            print("Path found: ", steps, " steps!")

        for i in range(4):
            runner = Runner(i);
            if runner.ID == 0:
                runner.runLeft(maze, start, end, steps)
            elif runner.ID == 1:
                runner.runRight(maze, start, end, steps)
            elif runner.ID == 2:
                runner.runUp(maze, start, end, steps)
            else:
                runner.runDown(maze, start, end, steps)

    def runLeft(self, maze, start, end, steps):

        path = maze
        left = (start[1] - 1)

        if not ((left < 0) or (path[start[0]][left])):
            path[start[0]][start[1]] = '<'
            start = (start[0], left)
            steps += 1
            Runner.run(path, start, end, steps)

    def runRight(self, maze, start, end, steps):

        path = maze
        right = (start[1] + 1)

        if not ((right > len(path) - 1) or (path[start[0]][right])):
            path[start[0]][start[1]] = '>'
            start = (start[0], right)
            steps += 1
            Runner.run(path, start, end, steps)

    def runUp(self, maze, start, end, steps):

        path = maze
        up = (start[0] - 1)

        if not ((up < 0) or (path[up][start[1]])):
            path[start[0]][start[1]] = '^'
            start = (up, start[1])
            steps += 1
            Runner.run(path, start, end, steps)

    def runDown(self, maze, start, end, steps):

        path = maze
        down = (start[0] + 1)

        if not ((down > len(path) - 1) or (path[down][start[1]])):
            path[start[0]][start[1]] = 'v'
            start = (down, start[1])
            steps += 1
            Runner.run(path, start, end, steps)

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

originRunner = Runner(99)
originRunner.run(maze, start, end, 0)

"""""
print("Maze:")
for i in range(len(maze)):
    print(maze[i])

print("")
"""