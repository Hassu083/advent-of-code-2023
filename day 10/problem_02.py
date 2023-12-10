import sys
# import matplotlib.path as mpltPath

# print(sys.getrecursionlimit())
f = open("e://advent of code//day 10//problem_02.txt")


game = [list(line.strip()) for line in f.readlines()]
sys.setrecursionlimit(len(game)*len(game[0])*1000)
# print(sys.getrecursionlimit())
dirs = {
    "S": [(1, 0), (0, 1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    ".":[],
    "0":[]
}
# zeroArea = 0
def dfs(i, j, step = 0, visited = set()):

    if game[i][j] == 'S':
        # global zeroArea
        # zeroArea = step
        print((step+1)//2)  

    for x, y in dirs[game[i][j]]:
        newi, newy = i+x, j+y
        if (newi, newy) not in visited and 0<=newi<len(game) and 0<=newy<len(game[0]):
            visited.add((newi,newy))
            dfs(newi, newy, step+1, visited)



# def countNode(i, j ):
#     game[i][j] = "#"
#     ans = 0
#     for x,y in [(1,0),(0,1),(0,-1),(-1,0)]:
#         newx, newy = i+x, j+y
#         if 0<=newx<len(game) and 0<=newy<len(game[0]) and game[newi][newy] not in ['0','#']:
#             ans += 1 + countNode(newx, newy)

#     return ans

visited = set()
for i in range(len(game)):
    for j in range(len(game[0])):
        if game[i][j] == 'S':
            for x, y in dirs[game[i][j]]:
                newi, newy = i+x, j+y
                visited = {(newi,newy)}
                dfs(newi,newy,1,visited)
            game[i][j] = "F"
            break





# for i, j in visited:
#     game[i][j] = "0"

# def ray_tracing(x,y,poly):
#     n = len(poly)
#     inside = False
#     p2x = 0.0
#     p2y = 0.0
#     xints = 0.0
#     p1x,p1y = poly[0]
#     for i in range(n+1):
#         p2x,p2y = poly[i % n]
#         if y > min(p1y,p2y):
#             if y <= max(p1y,p2y):
#                 if x <= max(p1x,p2x):
#                     if p1y != p2y:
#                         xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
#                     if p1x == p2x or x <= xints:
#                         inside = not inside
#         p1x,p1y = p2x,p2y

#     return inside


for i in range(len(game)):
    for j in range(len(game[0])):
        if (i,j) not in visited:
            game[i][j] = "0"


# poly  = list(visited)
# ans = 0
# for i in range(len(game)):
#     for j in range(len(game[0])):
#         if game[i][j] != '0':
#             ans += ray_tracing(i,j,poly)
# print(ans)

# path = mpltPath.Path(poly)
# ans = 0
# for i in range(len(game)):
#     for j in range(len(game[0])):
#         if game[i][j] != '0':
#             ans += sum(path.contains_points([(i,j)]))
# print(ans)
# totalArea = len(game)*len(game[0])
# otherthanzero = 0
# for i in [0,len(game)-1]:
#     for j in range(len(game[0])):
#         if game[i][j] not in ['0','#']:
#             otherthanzero += countNode(i, j) + 1

# for i in range(len(game)):
#     for j in [0,len(game[0])-1]:
#         if game[i][j] not in ['0','#']:
#             otherthanzero += countNode(i, j) + 1

# print(totalArea, otherthanzero, zeroArea)
# print(totalArea-otherthanzero-zeroArea)


ans = 0
inside = set()
for i in range(len(game)):
    count = 0
    for j in range(len(game[0])):
        if game[i][j] == '0' and count%2:
            ans += 1
            inside.add((i,j))
        elif game[i][j] in {'|','J','L'}: # {'|','F','7'}
            count += 1 
print(ans)
for i, j in inside:
    game[i][j] = "#"


f = open("Day 10//out.txt", "w")
for line in game:
    f.write("".join(line)+"\n")
 



            
