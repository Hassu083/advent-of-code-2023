f = open("e://advent of code//day 09//problem_02.txt")


lines = f.readlines()
ans = 0
for sequence in lines:
    sequence = list(map(int, sequence.strip().split(' ')))
    required = sequence
    to_ans = [sequence[0]]
    while any(val != 0 for val in required):
    
        new_required = []
        for i in range(1,len(required)):
            new_required.append(required[i]-required[i-1])
        required = new_required
        if required:
            to_ans.append(required[0])
    temp = 0
    for i in range(len(to_ans)-1,0,-1):
        to_ans[i-1] -= to_ans[i]
    
    ans += to_ans[0]

print(ans)