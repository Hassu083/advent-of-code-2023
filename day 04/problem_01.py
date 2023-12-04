f = open("e://advent of code//day 04//problem_01.txt")

ans = 0
FILTER = lambda x : x
for card in f:

    _, numbers = card.split(":")
    numbers = numbers.strip()
    winning, i_have = numbers.split('|')
    winning = set(filter(FILTER, winning.split(' ')))
    i_have = list(filter(FILTER, i_have.split(' ')))
    points = 0
    for number in i_have:
        if number in winning:
             points = 1 if points == 0 else points*2

    ans += points

print(ans)


