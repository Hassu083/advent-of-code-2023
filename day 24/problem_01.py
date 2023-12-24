
f = open("e://advent of code//day 24//problem_01.txt")

inp = [i.strip().replace("@",",") for i in f.read().split("\n")]
tas = 200000000000000
tae = 400000000000000

lines = []
for line in inp:
	x,y,z,vx,vy,vz = map(int,line.split(","))
	lines.append((x,y,vx,vy,vy/vx))

count = 0
for i, (x,y,vx,vy,m) in enumerate(lines):
	for j, (x1,y1,vx1,vy1,m1) in enumerate(lines[i+1:]):
		if m == m1:
			continue
		mx1 = m*x
		mx2 = m1*x1
		int_x = (mx1-y-mx2+y1)/(m-m1)
		mx = m*int_x
		int_y = mx-mx1+y
		if not (tas <= int_x <= tae) or not (tas <= int_y <= tae):
			continue
		
		if (vx < 0 and int_x > x) or (vy < 0 and int_y > y) or (vx1 < 0 and int_x > x1) or (vy1 < 0 and int_y > y1) or (vx > 0 and int_x < x) or (vy > 0 and int_y < y) or (vx1 > 0 and int_x < x1) or (vy1 > 0 and int_y < y1):
			continue
		
		count += 1

print(count)








