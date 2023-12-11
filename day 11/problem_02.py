import math
f = open("e://advent of code//day 11//problem_02.txt")


lines = f.readlines()
numberOfrows = len(lines)
numberOfcol = len(lines[-1])
rows = set([i for i in range(numberOfrows)])
cols = set([i for i in range(numberOfcol)])
ans = 0
positions = []
for i in range(numberOfrows):
    for j in range(numberOfcol):
        if lines[i][j] == "#":
            positions.append((i,j))
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)

n = len(positions)
for p1 in range(n):
    for p2 in range(p1, n):
        x1, y1 = positions[p1]
        x2, y2 = positions[p2]

        ans += abs(x2-x1) + abs(y2-y1)

        for extraRow in rows:
            if min(x1,x2) < extraRow < max(x1,x2):
                ans += 1000000-1
        for extraCol in cols:
            if min(y1,y2) < extraCol < max(y1,y2):
                ans += 1000000-1

            
print(ans)