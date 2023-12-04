f = open("e://advent of code//day 02//problem_01.txt")

ans = 0
_map = {"red":12, "green":13, "blue":14}

for line in f.readlines():

    gameid, game = line.split(':')
    _, gameid =  gameid.split(' ')

    for set in game.split(';'):

        for element in set.split(','):
            
            number, color = element.strip(' ').split(' ')

            if _map[color.strip()] < int(number):
                break
        else:
            continue
        break 
    else:
        ans += int(gameid)

print(ans)