n = int(input())
if (n % 2 == 1) or (6 <= n <= 20) or (n > 20 and n % 2 == 1):
	text_to_print = 'Weird'
else:
	text_to_print = 'Not Weird'
print(text_to_print)