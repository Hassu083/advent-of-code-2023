from collections import defaultdict

f = open("e://advent of code//day 15//problem_02.txt")


lines = f.read().strip().split(',')
ans = 0

def HASH(pattern):
    hashednumber = 0
    for char in pattern:
        hashednumber += ord(char)
        hashednumber *= 17
        hashednumber %= 256
    return hashednumber

boxes = [defaultdict(int) for _ in range(256)]


for p in lines:
    if p[-1] == "-":
        pattern = p[:-1]
        slot = boxes[HASH(pattern)]
        if pattern in slot:
            slot.pop(pattern)
    else:
        pattern, f = p.split("=")
        boxes[HASH(pattern)][pattern] = int(f)


for i in range(256):
    j = 1
    for key in boxes[i]:
        ans += (i+1)*j*boxes[i][key]
        j += 1

print(ans)