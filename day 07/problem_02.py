from collections import Counter
f = open("e://advent of code//day 07//problem_02.txt")


lines = f.readlines()


def power(card):
    card = card.replace('A', chr(61))
    card = card.replace('K', chr(60))
    card = card.replace('Q', chr(59))
    card = card.replace('J', '1')
    card = card.replace('T', chr(58))

    counter = Counter(card)
    
    j = counter['1']
    if j and j != 5:
        counter.pop('1')
        maxcount = ('',0)
        for key, val in counter.items():
            if maxcount[1]<val:
                maxcount = (key, val)
        counter[maxcount[0]] += j

    n = len(counter)
        
    if (n == 5):
        return 1, card
    elif n == 1:
        return 7, card
    elif n == 4:
        return 2, card
    elif n == 3:
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

ans = 0
for rank in range(len(cards)):
    ans += (rank+1)*cards[rank][1]
print(ans)