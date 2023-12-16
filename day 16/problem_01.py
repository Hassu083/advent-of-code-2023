from sys import setrecursionlimit
f = open("e://advent of code//day 16//problem_01.txt")

lines = [list(i.strip()) for i in f.readlines()]


n = len(lines)
m = len(lines[0])

setrecursionlimit(n*m)


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

visited = set()
visited_directions = set()

def Dfs(i, j, dir, pattern):
    if 0 <= i < n and  0<= j < m:
         visited.add((i,j))
         visited_directions.add((i,j, dir))
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
        
Dfs(0, 0, "R", lines)        

print((len(visited)))

