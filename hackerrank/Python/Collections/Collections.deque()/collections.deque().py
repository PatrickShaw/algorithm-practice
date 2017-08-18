import collections
n = int(input())
a_deque = collections.deque()
for _ in range(n):
	command = input().split()
	action = command[0]
	if action == 'append':
		a_deque.append(command[1])
	elif action == 'appendleft':
		a_deque.appendleft(command[1])
	elif action == 'pop':
		a_deque.pop()
	elif action == 'popleft':
		a_deque.popleft()
print(" ".join([x for x in a_deque]))		