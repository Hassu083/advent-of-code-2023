from collections import Counter
f = open("e://advent of code//day 07//problem_01.txt")


lines = f.readlines()


def power(card):
    card = card.replace('A', chr(62))
    card = card.replace('K', chr(61))
    card = card.replace('Q', chr(60))
    card = card.replace('J', chr(59))
    card = card.replace('T', chr(58))

    counter = Counter(card)

    if len(counter) == 5:
        return 1, card
    elif len(counter) == 1:
        return 7, card
    elif len(counter) == 4:
        return 2, card
    elif len(counter) == 3:
        if 3 in counter.values():
            return 4, card
        else:
            return 3, card
    elif 3 in counter.values():
        return 5, card
    else:
        return 6, card

cards = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
cards.sort(key= lambda x : power(x[0]))
# print(cards)

ans = 0
for rank in range(len(cards)):
    ans += (rank+1)*cards[rank][1]
print(ans)