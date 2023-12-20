from collections import deque
from math import lcm

f = open("e://advent of code//day 20//problem_02.txt")
circuit_flow = f.readlines()

def evaluate_flipflop(ff, recieve):
    if recieve == 1:
        return
    components[ff][1] = 0 if components[ff][1] else 1
    output = components[ff][1]
    Q.append((ff, output))

def evaluate_conjunction(source, con, recieve):
    if source in components[con][2]:
        if recieve == 0:
            components[con][2].remove(source)
            components[con][3].add(source)
    else:
        if recieve == 1:
            components[con][3].remove(source)
            components[con][2].add(source)
    
    n1, n2 = len(components[con][2]), len(components[con][3])
    output = 0 if n2==0 else 1
    Q.append((con, output))

components = {}
connections = {}
conjunctions = []

for circuit in circuit_flow:
    before, after = circuit.strip().split(' -> ')
    if before[0] == "%":
        before = before[1:]
        components[before] = [1, 0]  # type , state
    elif before[0] == "&":
        before = before[1:]
        conjunctions.append(before)
        components[before] = [0, 0, set(), set()]  # type , state, inputOne, inputZero
    connections[before] = after.split(', ')

for conjunction in conjunctions:
    for component in connections:
        if conjunction in connections[component]:
            components[conjunction][-1].add(component)

inputTorx = [i for i in connections if 'rx' in connections[i]][0]
inputToinputTorx = {i: 0 for i in connections if inputTorx in connections[i]}
presses = 0
flag = False

while True:
    presses += 1
    Q = deque([('broadcaster', 0)])
    while Q:
        component, pulse = Q.popleft()

        if component in inputToinputTorx and pulse:
            if inputToinputTorx[component]==0:
                inputToinputTorx[component] = presses

        if all(inputToinputTorx.values()):
            flag = True
            break

        for next_component in connections[component]:
            if next_component not in components: continue
            if components[next_component][0] == 1:
                evaluate_flipflop(next_component, pulse)
            else:
                evaluate_conjunction(component, next_component, pulse)
    
    if flag:
        break

# Repeating cycyles
# ({'th': [3947, 7894, 11841], 'sv': [4001, 8002, 12003], 'gh': [3943, 7886, 11829], 'ch': [3917, 7834, 11751]})
ans = 1
for val in inputToinputTorx.values():
    ans = lcm(ans, val)
print(ans)









    