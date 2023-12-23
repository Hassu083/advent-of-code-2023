from sys import setrecursionlimit
   
f = open("e://advent of code//day 23//problem_01.txt")
graph = [i.strip() for i in f.readlines()]
n = len(graph)
m = len(graph[0])
setrecursionlimit(n*m)

directions = {
    '>':[(0,1)],
    '<':[(0,-1)],
    '^':[(-1,0)],
    'v':[(1,0)],
    '.':[(1,0),(0,1),(-1,0),(0,-1)]
}

def dfs(i, j, distance = 0, visited = set()):
    if i == n-1 and j == m - 2:
        return distance
        
    if 0<= i < n and 0 <= j < m and graph[i][j] != '#' and (i,j) not in visited:
        visited.add((i, j))
        
        ans = 0
        for di, dj in directions[graph[i][j]]:
            ans = max(ans, dfs(i+di, j+dj, distance+1, visited = visited))

        visited.remove((i,j))

        return ans
    return 0

print(dfs(0,1,0, set()))
            
    










