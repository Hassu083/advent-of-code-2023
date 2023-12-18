f = open("e://advent of code//day 18//problem_02.txt")

lines = f.readlines()


direction = {
    "0" : (0,1),
    "3" : (-1,0),
    "2" : (0,-1),
    "1" : (1,0),
}

def hexaTodecimal(h):
    decimal = 0
    mapping = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    n = len(h)-1
    for i in range(n,-1,-1):
        decimal += mapping[h[i]]*(16**(n-i))
    return decimal

points = []

currentRow = 0
currentColunm = 0
perimeter = 0

for line in lines:
    _, _, dirSteps = line.split(' ')
    dirSteps = dirSteps.strip()[2:-1]
    dir_ = dirSteps[-1]
    steps = hexaTodecimal(dirSteps[:-1])
    perimeter += steps
    currentRow += direction[dir_][0]*steps
    currentColunm += direction[dir_][1]*steps
    points.append((currentRow, currentColunm))

area = 0
for (x1, y1), (x2, y2) in zip(points[1:],points[:-1]):
    area += (y1+y2)*(x1-x2)

print(area//2+perimeter//2+1)

