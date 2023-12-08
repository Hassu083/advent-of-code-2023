import math
f = open("e://advent of code//day 08//problem_02.txt")


lines = f.readlines()
instrution = lines[0].strip()
n = len(instrution)
graph = {}
starts = []
for line in lines[2:]:
    soure, _, d1, d2 = line.strip().split(' ')
    if soure[-1] == 'A':
        starts.append(soure)
    graph[soure] = [d1[1:-1], d2[:-1]]

def traverse(currentPostion):
    steps = 0
    while currentPostion[-1] != 'Z':
        index = 0 if instrution[steps%n] == 'L' else 1
        currentPostion = graph[currentPostion][index]
        steps += 1
    return steps

ans = 1
for start in starts:
    ans = math.lcm(ans, traverse(start))
print(ans)