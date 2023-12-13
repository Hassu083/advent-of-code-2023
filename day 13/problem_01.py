f = open("e://advent of code//day 13//problem_01.txt")


lines = f.read().split("\n\n")
ans = 0


def solve(pattern, multiplying_factor):

    n = len(pattern)
    for sel_row in range(n-1):
        flag = True
        for range_ in range(n//2):
            left = sel_row-range_
            right = sel_row+range_+1
            if 0 <= left < right < n:
                for col in range(len(pattern[0])):
                    if pattern[left][col] != pattern[right][col]:
                        flag = False
                        break
        if flag:
            return (sel_row+1)*multiplying_factor
    return 0



for pattern in lines:
    pattern = pattern.split("\n")
    ans += solve(list(zip(*pattern)),1)
    ans += solve(pattern,100)

print(ans)