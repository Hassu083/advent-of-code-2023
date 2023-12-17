from heapq import heappush, heappop
from collections import defaultdict


f = open("e://advent of code//day 17//problem_02.txt")

graph = [list(map(int, list(i.strip()))) for i in f.readlines()]
ans = float("inf")

n = len(graph)
m = len(graph[0])
heats = defaultdict(lambda : float("inf"))


direction = {
    "R" : [(0,1,"R"),(1,0,"D"),(-1,0,"U")],
    "U" : [(0,1,"R"),(0,-1,"L"),(-1,0,"U")],
    "L" : [(1,0,"D"),(0,-1,"L"),(-1,0,"U")],
    "D" : [(0,1,"R"),(0,-1,"L"),(1,0,"D")],
}


q = [(0, 0, 0, 0, "R")] #   heat, i, j, move count, direction    



while q:
    heat, i, j, move_count, direc = heappop(q)

    if heats[(i,j, direc, move_count)] < heat:
        continue

    if i == n-1 and j == m-1 and move_count >= 4:
        ans = min(ans, heat)

    for di, dj, dir_ in direction[direc]:
        if (move_count >= 10 and direc == dir_) or (move_count < 4 and direc != dir_): continue
        newi, newj = i+di, j+dj
        if 0<=newi<n and 0<=newj<m:
            newHeat = heat+graph[newi][newj]
            new_move_count = move_count+1 if direc == dir_ else 1
            if newHeat <  heats[(newi,newj, dir_, new_move_count)]:
                heats[(newi,newj, dir_,new_move_count)] = newHeat
                heappush(q, (newHeat, newi, newj, new_move_count, dir_))


print(ans)
