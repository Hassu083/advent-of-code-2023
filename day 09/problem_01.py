f = open("e://advent of code//day 09//problem_01.txt")


lines = f.readlines()
ans = 0
for sequence in lines:
    sequence = list(map(int, sequence.strip().split(' ')))
    required = sequence
    to_ans = sequence[-1]
    while any(val != 0 for val in required):
    
        new_required = []
        for i in range(1,len(required)):
            new_required.append(required[i]-required[i-1])
        required = new_required
        if required:
            to_ans += required[-1]

    ans += to_ans

print(ans)