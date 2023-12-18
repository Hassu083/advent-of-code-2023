f = open("e://advent of code//day 18//problem_01.txt")

lines = f.readlines()


direction = {
    "R" : (0,1),
    "U" : (-1,0),
    "L" : (0,-1),
    "D" : (1,0),
}

points = []

currentRow = 0
currentColunm = 0
perimeter = 0

for line in lines:
    dir_, steps, _ = line.split(' ')
    steps = int(steps)
    perimeter += steps
    currentRow += direction[dir_][0]*steps
    currentColunm += direction[dir_][1]*steps
    points.append((currentRow, currentColunm))

area = 0
for (x1, y1), (x2, y2) in zip(points[:-1],points[1:]):
    area += ((y1+y2)*(x1-x2))

print(abs(area)//2+perimeter//2+1)

