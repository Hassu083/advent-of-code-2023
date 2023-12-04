f = open("e://advent of code//day 02//problem_02.txt")

ans = 0

for line in f.readlines():

    _, game = line.split(':')
    
    _map = {'red':0, 'green':0, 'blue':0}

    for set in game.split(';'):

        for element in set.split(','):
            
            number, color = element.strip(' ').split(' ')
            color = color.strip()
            _map[color] = max(_map[color], int(number))
    
    ans += _map['red']*_map['green']*_map['blue']

print(ans)