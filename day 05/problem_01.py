f = open("e://advent of code//day 05//problem_01.txt")


lines = f.readlines()
n = len(lines)
_, sources = lines[0].split(':')
sources = list(map(int, sources.strip().split(' ')))


i = 1
while i<n:
    i += 2
    destination = []
    visited= set()
    while i<n and lines[i] != '\n':
        d_map_sart, source_map_s, end_range = map(int, lines[i].split(' '))
        source_end = source_map_s+end_range-1
        for source in sources:
            if source in visited: continue
            if source_map_s <= source <= source_end:
                destination.append(d_map_sart+source-source_map_s)
                visited.add(source)
        i += 1
    
    for source in sources:
        if source not in visited:
            destination.append(source)

    sources = destination

    

   
print(min(sources))


