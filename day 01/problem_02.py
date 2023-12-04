f = open("e://advent of code//day 01//problem_02.txt")

ans = 0
number = ''
for line in f.readlines():

    number = ''
    for i, word in enumerate(line):

        if word in '0123456789':
            number += word
        
        for index, digit in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
            if line[i:i+len(digit)] == digit:
                number += str(index)
                
    ans += int(number[0]+number[-1])

print(ans)