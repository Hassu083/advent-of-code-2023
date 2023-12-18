f = open("e://advent of code//day 14//problem_01.txt")


lines = f.readlines()
ans = 0

n = len(lines)
m = len(lines[0])-1
ansForRow = [n]*m

for i, row in enumerate(lines):
    for j in range(m):
        if lines[i][j] == "#":
            ansForRow[j] = n-i-1
        elif lines[i][j] == "O":
            ans += ansForRow[j]
            ansForRow[j] -= 1

print(ans)





