f = open("e://advent of code//day 01//problem_01.txt")

ans = 0
number = ''
for line in f:
    number = ''
    for word in line:

        if word in '0123456789':
            number += word
    ans += int(number[0]+number[-1])

print(ans)