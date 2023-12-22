from collections import deque
from math import ceil

f = open("e://advent of code//day 21//problem_02.txt")

garden = f.readlines()
n = len(garden)
m = len(garden[0])-1

Q = deque([])
for i in range(n):
    for j in range(m):
        if garden[i][j] == "S":
            Q.append((i, j))
            break

def mapXY(x, y):
    if x>=n:
        x %= n
    elif x<0:
        multiplying_term = ceil(abs(x)/(n))
        x += n*multiplying_term
    if y>=m:
        y %= m
    elif y<0:
        multiplying_term = ceil(abs(y)/m)
        y += m*multiplying_term
    return x,y

for steps in range(328):
    visited = set()
    for i in range(len(Q)):
        x, y = Q.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            actualx, actualy = x+dx, y+dy
            newx,newy = mapXY(actualx, actualy)
            if garden[newx][newy] != "#" and (actualx, actualy) not in visited:
                value = (actualx,actualy)
                visited.add(value)
                Q.append(value)
    if steps in [65,196,327]:
        print(steps,':', len(visited))



x_to_f = {
    65 : 3981,
    # 131 : 15497,
    196 : 34557,
    327 : 95265
    # 261 : 60675
}
# print(x_to_f)

x_to_solve = 261

goal = 26501365
def f(n):
    a0 = 3797
    a1 = 34009
    a2 = 94353

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
print(f(goal//n))


