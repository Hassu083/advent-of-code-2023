f = open("e://advent of code//day 04//problem_02.txt")

ans = 0
FILTER = lambda x : x
cards = f.readlines()
n = len(cards)-1
extra_copies = [0]*(n+1)

for i, card in enumerate(cards):

    _, numbers = card.split(":")
    numbers = numbers.strip()
    winning, i_have = numbers.split('|')
    winning = set(filter(FILTER, winning.split(' ')))
    i_have = list(filter(FILTER, i_have.split(' ')))
    extra_copies[i] += extra_copies[i-1] if i-1 >= 0 else 0
    copies = extra_copies[i]+1
    numberOfWin = 0
    for number in i_have:
        if number in winning:
            numberOfWin += 1
    next_ = i+1
    end = next_ + numberOfWin
    if next_ <= n:
        extra_copies[next_] += copies
    if end <= n:    
        extra_copies[end] -= copies

    ans += extra_copies[i] + 1

print(ans)


