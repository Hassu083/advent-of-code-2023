from collections import  defaultdict
   
f = open("e://advent of code//day 22//problem_01.txt")
lines = f.readlines()

def checkOverlap(i ,*points):
    (x,y),(x1,y1) = points
    for (x_,y_),(x1_,y1_),_ in stack[i]:
        if ( max(x, x_) <= min(x1, x1_) and max(y, y_) <= min(y1, y1_) ):
            return True
    return False

def markOverlap(i, *point):
    (x,y),(x1,y1), name = point
    for (x_,y_),(x1_,y1_),name_ in stack[i]:
        if ( max(x, x_) <= min(x1, x1_) and max(y, y_) <= min(y1, y1_) ):
            if name not in supports:
                supports[name] = []
            if name_ not in supportedBy:
                supportedBy[name_] = []
            if name != name_:
                supports[name].append(name_)
                supportedBy[name_].append(name)

bricks = []
for line in lines:
    before, after = line.split('~')
    x, y, z = map(int,before.split(','))
    x1, y1, z1 = map(int, after.split(','))
    bricks.append((z,x,y,z1,x1,y1))

supports = defaultdict(list)
supportedBy = defaultdict(list)

bricks.sort(key = lambda x:x[0])

brickName = 1
stack = []
for z,x,y,z1,x1,y1 in bricks:
    j = len(stack)-1
    while j >= 0 and (not checkOverlap(j,(x,y),(x1,y1))):
        j -= 1
    if j < 0:
        j = 0
    else:
        j += 1
    for i in range(j, j+z1-z+1):
        if len(stack) < i+1:
            stack.append([])
        stack[i].append([(x,y),(x1,y1),brickName])

    brickName += 1

supportedBy = {name: [] for (x,y),(x1,y1), name in stack[0]}

for i in range(len(stack)-1):
    for point in stack[i]:
        markOverlap(i+1, *point)

ans = 0
for i in range(1,len(bricks)+1):
    for suport in supports[i]:
        if len(supportedBy[suport]) == 1:
            break
    else:
        ans += 1

print(ans)









