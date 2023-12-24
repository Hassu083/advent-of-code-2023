from z3 import Real,Solver

f = open("e://advent of code//day 24//problem_01.txt")

inp = [i.strip().replace("@",",") for i in f.read().split("\n")]


x1,y1,z1,vx1,vy1,vz1 = Real('x'),Real('y'),Real('z'),Real('vx'),Real('vy'),Real('vz')
solver = Solver()

for i, line in enumerate(inp):
	x,y,z,vx,vy,vz = map(int,line.split(","))
	t = Real(f't{i}')
	solver.add(t>=0)
	solver.add(x+vx*t == x1+vx1*t)
	solver.add(y+vy*t == y1+vy1*t)
	solver.add(z+vz*t == z1+vz1*t)
print(solver.check())
model = solver.model()
print(model.eval(x1).as_long()+model.eval(y1).as_long()+model.eval(z1).as_long())








