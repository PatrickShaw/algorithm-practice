from collections import OrderedDict
n = int(input())
word_occurances = OrderedDict()
for _ in range(n):
	word = input()
	word_occurances[word] = word_occurances[word] + 1 if word in word_occurances else 1
print(len(word_occurances))
print(' '.join([str(x[1]) for x in word_occurances.items()]))