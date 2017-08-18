import math
n = int(input())
for _ in range(n):
	inputs = input().split()
	p_x = int(inputs[0])
	p_y = int(inputs[1])

	q_x = int(inputs[2])
	q_y = int(inputs[3])

	d_x = p_x - q_x 
	d_y = p_y - q_y
	o_x = 0
	o_y = 0
	if d_x == 0:
		o_x = p_x
		o_y = d_y * -2 + p_y
	else:
		g = d_y / d_x
	
		o_x = (d_x * -2) + p_x
		o_y = (d_x * -2) * g + p_y
	print('%s %s' % (o_x, int(o_y)))