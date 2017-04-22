def array_left_rotation(a, n, k):
	start_index = k % n
	return a[start_index:] + a[:start_index]


n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

