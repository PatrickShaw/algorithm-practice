P = input()
valid = len(P) == 6
try:
    int(P)
except:
    valid = False
noRepeats = 0
for i in range(len(P)-2):
    noRepeats += P[i] == P[i+2]
valid = valid and noRepeats <= 1
print(valid)