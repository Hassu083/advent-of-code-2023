f = open("e://advent of code//day 15//problem_01.txt")


lines = f.read().strip().split(',')
ans = 0

def HASH(pattern):
    hashednumber = 0
    for char in pattern:
        hashednumber += ord(char)
        hashednumber *= 17
        hashednumber %= 256
    return hashednumber



for pattern in lines:
    ans += HASH(pattern)

print(ans)