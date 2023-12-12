
f = open("e://advent of code//day 12//problem_02.txt")


lines = f.readlines()
ans = 0

def numberOfWays(count:int, i:int, j:int)-> int:
    # if i >= len(nums):
    #     return 1 if all(char[k] != "#" for k in range(j, len(char))) and count == 0 else 0
    if j >= len(char):
        return ((i >= len(nums) and count == 0) or (i == len(nums)-1 and  count == nums[i]))
  
    if (count, i, j) in dp:
        return dp[(count, i, j)]
    
    ans = 0
    for c in '#.':
        if char[j] == c or char[j] == '?':
            if c == ".":
                if i < len(nums) and count == nums[i]:
                    ans += numberOfWays( 0, i+1, j+1)
                elif count==0:
                    ans += numberOfWays(0, i, j+1)
            elif c == "#":
                ans += numberOfWays(count+1, i, j+1)

    dp[(count, i, j)] = ans
    return dp[(count, i, j)]


for line in lines:

    char, nums = line.strip().split(" ")
    char = "?".join([char]*5)
    nums = ",".join([nums]*5)
    nums = list(map(int, nums.split(",")))
  
    # print(numberOfWays(None, 0,0,0))
    dp = {}
    ans += numberOfWays(0,0,0)
{(0, 2): 14, (0, 1): 14, (2, 11): 0, (2, 10): 1, (2, 9): 2, (2, 8): 3, (2, 7): 4, (1, 11): 0, (1, 10): 0,
  (1, 9): 0, (1, 8): 1, (1, 7): 3, (1, 6): 7, (1, 5): 14, (1, 4): 14, (0, 3): 14, (0, 0): 14}

print(ans)