f = open("e://advent of code//day 19//problem_01.txt")

workflows, values = f.read().split('\n\n')
workflows = [i.strip() for i in workflows.split('\n')]
values = [i[1:-1].strip() for i in values.split('\n')]
ans = 0

class WorkFlow:

    def __init__(self, text) -> None:
        self.vars, self.conditions, self.values, self.TRUE, self.FALSE  = [], [], [], [], ""
        self.extract(text)
    
    def evaluate(self, mapping):
        for i, condition in enumerate(self.conditions):
            val_1 = mapping[self.vars[i]]
            val_2 = self.values[i]
            if self.solve(condition, val_1, val_2):
                return self.TRUE[i]
        return self.FALSE

    def solve(self, conditions, a, b):
        mapping = {'>':a>b, '<':a<b}
        return mapping[conditions]

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

for value in values:
    mapping = {}
    subanswer = 0
    for variable_value in value.split(','):
        variable, value = variable_value.split("=")
        value = int(value)
        mapping[variable] = value
        subanswer += value

    start = 'in'
    while start not in ['A', 'R']:
        start = extracted_workflows[start].evaluate(mapping)
    
    if start == "A":
        ans += subanswer

print(ans)

    