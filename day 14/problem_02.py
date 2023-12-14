from copy import deepcopy
import time
f = open("e://advent of code//day 14//problem_02.txt")


grid = [list(i) for i in f.read().split('\n')]

def rotate(grid):
    for _ in range(4):
        grid = moveNorth(grid)
        grid = takeTranspose(grid)
        grid = interchange(grid)
    return grid

def takeTranspose(grid):
    n = len(grid)
    m = len(grid[0])
    transpose = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[j][i] = grid[i][j]
    
    return transpose

def interchange(grid):
    return [row[::-1] for row in grid]

def moveNorth(grid):
    m = len(grid[0])
    ansForRow = [0]*m
    for i, row in enumerate(grid):
        for j in range(m):
            if grid[i][j] == "#":
                ansForRow[j] = i + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[ansForRow[j]][j] = "O"
                ansForRow[j] += 1
    return grid
            
def score(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i, row in enumerate(grid):
        for j in range(m):
            if row[j] == "O":
                ans += n-i
    return ans


all_in_cycle = list()
seen = dict()
cycles = 1_000_000_000

for t in range(cycles):
    grid = rotate(grid)
    hash_grid= str(grid)
    if hash_grid in seen:
        cycles = cycles - seen[hash_grid]
        ans = all_in_cycle[seen[hash_grid]-1:][(cycles%(t-seen[hash_grid]))]
        break
    seen[hash_grid] = t 
    all_in_cycle.append(deepcopy(grid))

print(score(ans))