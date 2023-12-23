from sys import setrecursionlimit

f = open("e://advent of code//day 23//problem_01.txt")
g = [i.strip() for i in f.readlines()]
n = len(g)
m = len(g[0])
setrecursionlimit(n*m)

DIR = [(1,0),(0,1),(-1,0),(0,-1)]
pointsOfInterest = set()  # for longest path (to avoid repeatition)

def validate(i,j):
    return 0<= i < n and 0 <= j < m

pointsOfInterest.add((0,1))
for i, row in enumerate(g):
    for j, val in enumerate(row):
        if val == '#':
            continue
        if sum([g[i+di][j+dj] != '#' for di, dj in DIR if validate(i+di, j+dj)]) >= 3:
            pointsOfInterest.add((i,j))
pointsOfInterest.add((n-1,m-2))            

graph = {point: {} for point in pointsOfInterest}

def addDistance(i, j,x, y, distance = 0, visited = set()):
    if (i,j) in pointsOfInterest and (i, j) != (x, y):
        graph[(x,y)][(i,j)] = distance
        return distance        
    if validate(i,j) and g[i][j] != '#' and (i,j) not in visited:
        visited.add((i, j))
        ans = 0
        for di, dj in DIR:
            ans = max(ans, addDistance(i+di, j+dj, x,y,  distance+1, visited = visited))
        return ans
    return 0

for i, j in pointsOfInterest:
    addDistance(i,j,i,j,0, set())

def dfs(i, j, visited):
    if (i, j) == (n-1, m-2):
        return 0
    visited.add((i, j))
    ans = 0
    for (ni, nj) in graph[(i,j)]:
        if (ni, nj) not in visited:
            ans = max(ans, dfs(ni,nj, visited)+graph[(i,j)][(ni,nj)])
    visited.remove((i, j))
    return ans

print(dfs(0, 1, set()))
            
    










