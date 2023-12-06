f = open("e://advent of code//day 06//problem_02.txt")


lines = f.readlines()

time  = int(''.join(map(str.strip, lines[0][10:].strip().split('  '))))
distance  = int(''.join(map(str.strip, lines[1][10:].strip().split('  '))))
print(time,distance)
totalways = 1

def f(x, y):
    ways = 0
    for i in range(1,x+1):
        if i*(x-i) > y:
            ways += 1
    return ways


print(f(time, distance))