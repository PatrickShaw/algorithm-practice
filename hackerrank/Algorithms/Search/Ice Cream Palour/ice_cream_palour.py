t = int(input())
for _ in range(t):
	money = int(input())
	n = int(input())
	costs = (int(x) for x in input().split())
	complement_costs_needed = dict()
	for cost_index in range(n):
		cost = next(costs)
		if cost in complement_costs_needed:
			print("%s %s" % (complement_costs_needed[cost] + 1, cost_index + 1))
			break
		complement_costs_needed[money - cost] = cost_index
		
