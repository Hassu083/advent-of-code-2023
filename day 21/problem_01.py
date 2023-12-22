from collections import deque

f = open("e://advent of code//day 21//problem_01.txt")
garden = f.readlines()
n = len(garden)
m = len(garden[0])-1

Q = deque([])

for i in range(n):
    for j in range(m):
        if garden[i][j] == "S":
            Q.append((i, j))
            break

visited = set()

for _ in range(64):
    visited = set()
    for i in range(len(Q)):
        x, y = Q.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            newx, newy = x+dx, y+dy
            if 0<=newx<n and 0<=newy<m and garden[newx][newy] != "#" and (newx, newy) not in visited:
                value = (newx,newy)
                visited.add(value)
                Q.append(value)

print(len(visited))