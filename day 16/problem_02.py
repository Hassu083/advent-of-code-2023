from sys import setrecursionlimit
f = open("e://advent of code//day 16//problem_02.txt")

lines = [list(i.strip()) for i in f.readlines()]
ans = 0


n = len(lines)
m = len(lines[0])

setrecursionlimit(n*m*100)


direction_to_origin = {
    "R":(0, 1),
    "L":(0, -1),
    "U":(-1, 0),
    "D": (1, 0),
}

direction = {
    ("R", "/"):["U"],
    ("L", "/"): ["D"],
    ("U", "/"):["R"],
    ("D", "/"):[ "L"],
    ("R", "\\"):["D"],
    ("L", "\\"):["U"],
    ("U", "\\"):["L"],
    ("D", "\\"):["R"],
    ("R", "|"):["D", "U"],
    ("L", "|"):["D", "U"],
    ("U", "-"):["L", "R"],
    ("D", "-"):["L", "R"],
}


def Dfs(i, j, dir, pattern):
    if 0 <= i < n and  0<= j < m:
         visited.add((i,j))
         key_ = (i,j, dir)
         visited_directions.add(key_)
         element = pattern[i][j]
         key = (dir, element)
         if key in direction:
             for newDir in direction[key]:
                 di, dj = direction_to_origin[newDir]
                 newi, newj = i+di, j+dj
                 if (newi, newj, newDir) not in visited_directions:
                    Dfs(newi, newj, newDir, pattern)
                 
         else:
             di, dj = direction_to_origin[dir]
             newi, newj = i+di, j+dj
             if (newi, newj, dir) not in visited_directions:
                Dfs(newi, newj, dir, pattern)

        
  

for i in range(n):
    visited_directions = set()
    visited = set()
    Dfs(0, i, "D", lines)
    ans = max(ans, len(visited))
    visited_directions = set()
    visited = set()
    Dfs(n-1, i, "U", lines)
    ans = max(ans, len(visited))

for i in range(m):
    visited_directions = set()
    visited = set()
    Dfs(i, 0, "R", lines)
    ans = max(ans, len(visited))
    visited_directions = set()
    visited = set()
    Dfs(i, m-1, "L", lines)
    ans = max(ans, len(visited))


print(ans)

