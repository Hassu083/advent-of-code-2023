from collections import deque

f = open("e://advent of code//day 20//problem_01.txt")
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

visited = dict()
previous_ans = []

for i in range(1000):
    low =  1
    high = 0
    Q = deque([('broadcaster', 0)])
    while Q:
        component, pulse = Q.popleft()
        for next_component in connections[component]:
            if pulse:
                high += 1
            else:
                low +=  1
            if next_component not in components: continue
            if components[next_component][0] == 1:
                evaluate_flipflop(next_component, pulse)
            else:
                evaluate_conjunction(component, next_component, pulse)
    comp_str = str(components)
    if comp_str in visited:
        break
    visited[comp_str] = i
    previous_ans.append([low, high])

# total_pulses = 0
# total_button_press = 1000
# start = visited[comp_str]
# end = i
# before_l = 0
# before_h  = 0
# if start > 0:
#     total_button_press -= start
#     before_l += sum(previous_ans[:start][i][0] for i in range(start))
#     before_h += sum(previous_ans[:start][i][1] for i in range(start))
#     previous_ans = previous_ans[start:]
# cycle_size = end - start
# l_pulse_in_cycle = 0
# h_pulse_in_cycle = 0
# remaining_l = 0
# remaining_h = 0
# if cycle_size:
#     total_complete_cycle = total_button_press//cycle_size
#     l_pulse_in_cycle = sum(i[0] for i in previous_ans)*total_complete_cycle
#     h_pulse_in_cycle = sum(i[1] for i in previous_ans)*total_complete_cycle
#     remaining_l = sum(i[0] for i in previous_ans[:total_button_press%cycle_size])
#     remaining_h = sum(i[1] for i in previous_ans[:total_button_press%cycle_size])
# total_pulses = (before_l+l_pulse_in_cycle+remaining_l) * (before_h + h_pulse_in_cycle + remaining_h)
# print((before_l+l_pulse_in_cycle+remaining_l),(before_h + h_pulse_in_cycle + remaining_h))
# print(total_pulses)

before_l = sum(i[0] for i in previous_ans)
before_h = sum(i[1] for i in previous_ans)
print(before_l, before_h, before_h*before_l)