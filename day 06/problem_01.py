import math
f = open("e://advent of code//day 06//problem_01.txt")


lines = f.readlines()

times  = list(map(int, lines[0][10:].strip().split('   ')))
distances  = list(map(int, lines[1][10:].strip().split('   ')))
print(times,distances)
totalways = 1

# def f(x, y):
#     ways = 0
#     for i in range(1,x+1):
#         if i*(x-i) > y:
#             ways += 1
#     return ways

# for i in range(len(times)):
#     totalways *= f(times[i], distances[i])

def quadratic(x, y):
    common_term = math.sqrt(x*x - 4*y)
    x0 = math.ceil((x-common_term)/2)
    x1 = math.floor((x+common_term)/2)

    if x0*(x-x0) == y:
        x0 += 1
    if x1*(x-x1) == y:
        x1 -= 1
    
    return x1-x0+1

for i in range(len(times)):
    totalways *= quadratic(times[i], distances[i])

print(totalways)


