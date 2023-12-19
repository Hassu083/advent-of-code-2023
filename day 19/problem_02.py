from copy import deepcopy

f = open("e://advent of code//day 19//problem_02.txt")

workflows, _ = f.read().split('\n\n')
workflows = [i.strip() for i in workflows.split('\n')]
mapping = {'x':0,'m':1,'a':2,'s':3}


class WorkFlow:

    def __init__(self, text) -> None:
        self.vars, self.conditions, self.values, self.TRUE, self.FALSE  = [], [], [], [], ""
        self.extract(text)
    
    def extract(self, text):
        text = text.split(',')
        self.FALSE = text[-1]
        text = text[:-1]
        for val in text:
            expression, destination = val.split(":")
            variable = expression[0]
            condition = expression[1]
            value = int(expression[2:])
            self.vars.append(variable)
            self.conditions.append(condition)
            self.values.append(value)
            self.TRUE.append(destination)

extracted_workflows = {}
for workflow in workflows:
    name, text = workflow.split('{')
    extracted_workflows[name] = WorkFlow(text[:-1])

def tobeReturn(ranges):
    ans = 1
    for a,b in ranges:
        ans *= b-a+1
    return ans

def count(start = 'in', ranges = [[1,4000],[1,4000],[1,4000],[1,4000]]):
    if any((i[0] >  i[1])   for i in ranges):
        return 0
    if start == "A":
        return tobeReturn(ranges)
    elif start == "R":
        return 0
    ans = 0
    obj = extracted_workflows[start]
    for i, var in enumerate(obj.vars):
            j = mapping[var]
            TRUE, FALSE = name(obj, i)
            newRange, ranges = takeIntersection(TRUE, FALSE, ranges, j)
            ans += count(obj.TRUE[i], newRange)
    ans += count(obj.FALSE, ranges)

    return ans

def takeIntersection(range1, range2, range3, i):
    TRUE, FALSE = deepcopy(range3), deepcopy(range3)
    TRUE[i] =  [max(range1[0], TRUE[i][0]),min(range1[1], TRUE[i][1])]
    FALSE[i] =  [max(range2[0], FALSE[i][0]),min(range2[1], FALSE[i][1])]
    return TRUE, FALSE

def name(obj, i):
    if obj.conditions[i] == '>':
        return [obj.values[i]+1, 4000], [1, obj.values[i]]
    return  [1,obj.values[i]-1], [obj.values[i],4000]

print(count())
    