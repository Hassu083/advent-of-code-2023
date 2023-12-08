f = open("e://advent of code//day 08//problem_01.txt")


lines = f.readlines()
instrution = lines[0].strip()
n = len(instrution)
graph = {}

for line in lines[2:]:
    soure, _, d1, d2 = line.strip().split(' ')
    graph[soure] = [d1[1:-1], d2[:-1]]

currentPostion = 'AAA'
steps = 0
while currentPostion != 'ZZZ':
    index = 0 if instrution[steps%n] == 'L' else 1
    currentPostion = graph[currentPostion][index]
    steps += 1

print(steps)