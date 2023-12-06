f = open("e://advent of code//day 05//problem_02.txt")


lines = f.readlines()
n = len(lines)
_, source = lines[0].split(':')
source = list(map(int, source.strip().split(' ')))
sources = [(source[i],source[i+1]) for i in range(0, len(source), 2)]


i = 1
while i<n:
    i += 2
    destination = []
    visited= set()
    while i<n and lines[i] != '\n':

        d_map_start, s_map_start, end_range = map(int, lines[i].split(' '))
        s_map_end = s_map_start+end_range

        # j = 0
        # while True:

            # source_start, range = sources[j]
        for source_start, range in sources:

            source_end = source_start+range-1

            start_overlap = max(s_map_start, source_start)
            end_overlap = min(s_map_end, source_end)

            if start_overlap < end_overlap:
                
                new_start = d_map_start+start_overlap-s_map_start
                new_range = end_overlap-start_overlap+1

                # unoverlapped region
                # if source_start != start_overlap:
                #     before_start = source_start
                #     before_range = s_map_start-before_start
                #     sources.append((before_start, before_range))

                # if end_overlap != source_end:
                #     after_start = end_overlap+1
                #     after_end = source_end-after_start
                #     sources.append((after_start, after_end))

                destination.append((new_start, new_range))
                # visited.add(sources[j])
                visited.add((source_start, range))

            # j += 1
            # if j == len(sources):
                # break
       

        i += 1
    
    for source in sources:
        if source not in visited:
            destination.append(source)
    sources = destination

    

   
print(min(source[0] for source in sources))

