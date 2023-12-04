f = open("e://advent of code//day 03//problem_02.txt")

ans = 0
engine_schematic = f.readlines()
m = len(engine_schematic)-1
n = len(engine_schematic[0])-2

def dfs(i, j):
    number = 0
    while j-1 >= 0 and engine_schematic[i][j-1] in '1234567890':
        j -= 1
    fromcol = j
    while j <= n and engine_schematic[i][j] in '1234567890':
        number = number*10 + int(engine_schematic[i][j])
        j += 1
    return fromcol, j, number

def findGearNumber(i, index, n, m):
    prevrow = max(i-1, 0)
    nextrow = min(m, i+1)
    from_ = max(index-1, 0)
    to = min(n, index+1)
    number1 = 0
    number2 = 0

    for row in range(prevrow, nextrow+1):
        fromcol = -1
        tocol = -1
        for col in range(from_, to+1):
            if fromcol <= col <= tocol:
                continue
            if engine_schematic[row][col] in '0123456789':
                if not number1:
                    fromcol, tocol, number1 = dfs(row, col)
                elif not number2:
                    fromcol, tocol, number2 = dfs(row, col)
    
    return number1*number2
    

for i, line in enumerate(engine_schematic):

    for  index, word in enumerate(line):

        if word == '*':
            ans += findGearNumber(i, index, n, m)
    

print(ans)