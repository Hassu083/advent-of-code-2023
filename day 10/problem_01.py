import sys

print(sys.getrecursionlimit())
f = open("e://advent of code//day 10//problem_01.txt")


game = [line.strip() for line in f.readlines()]
sys.setrecursionlimit(len(game)*len(game[0]))
print(sys.getrecursionlimit())
dirs = {
    "S": [(1, 0), (0, 1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    ".":[]
}

def dfs(i, j, step = 0, visited = set()):

    if game[i][j] == 'S':
        print((step+1)//2)  

    for x, y in dirs[game[i][j]]:
        newi, newy = i+x, j+y
        if (newi, newy) not in visited and 0<=newi<len(game) and 0<=newy<len(game[0]):
            visited.add((newi,newy))
            dfs(newi, newy, step+1, visited)




for i in range(len(game)):
    for j in range(len(game[0])):
        if game[i][j] == 'S':
            for x, y in dirs[game[i][j]]:
                newi, newy = i+x, j+y
                visited = {(newi,newy)}
                dfs(newi,newy,1,visited)
            
