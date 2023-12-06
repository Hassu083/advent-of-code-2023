import math
f = open("e://advent of code//day 06//problem_02.txt")


lines = f.readlines()

time  = int(''.join(map(str.strip, lines[0][10:].strip().split('  '))))
distance  = int(''.join(map(str.strip, lines[1][10:].strip().split('  '))))
print(time,distance)
totalways = 1

# def f(x, y):
#     ways = 0
#     for i in range(1,x+1):
#         if i*(x-i) > y:
#             ways += 1
#     return ways

def f(x, y):
    common_term = math.sqrt(x*x - 4*y)
    x0 = math.ceil((x-common_term)/2)
    x1 = math.floor((x+common_term)/2)

    if x0*(x-x0) == y:
        x0 += 1
    if x1*(x-x1) == y:
        x1 -= 1
    
    return x1-x0+1


print(f(time, distance))