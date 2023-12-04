f = open("e://advent of code//day 03//problem_01.txt")

ans = 0
engine_schematic = f.readlines()
m = len(engine_schematic)-1
n = len(engine_schematic[0])-2

def findSpecialCharacter(i, index, start, n, m):
    prevrow = max(i-1, 0)
    nextrow = min(m, i+1)
    from_ = max(start-1, 0)
    to = min(n, index+1)

    if engine_schematic[i][from_] != '.' and engine_schematic[i][from_] not in '0123456789':
        return True
    if engine_schematic[i][to-1] != '.' and engine_schematic[i][to-1] not in '0123456789':
        return True
    for row in [prevrow, nextrow]:
        if row == 0 or row == m:
            continue
        for col in range(from_, to):
            if engine_schematic[row][col] != '.' and engine_schematic[row][col] not in '0123456789':
                return True
    return False
    

for i, line in enumerate(engine_schematic):

    start = -1
    found = False
    number = 0
    for  index, word in enumerate(line):

        if word in '0123456789':
            number = number*10 + int(word)
            if start == -1:
                start = index
        elif start != -1:
            found = findSpecialCharacter(i, index, start, n, m)
            start = -1
            if found:
                found = False
                ans += number
            number = 0
    
    if start != -1:
        found = findSpecialCharacter(i, index, start, n, m)
        if found:
            ans += number

print(ans)