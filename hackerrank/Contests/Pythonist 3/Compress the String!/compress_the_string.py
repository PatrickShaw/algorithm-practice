S = input()
things = []
curr = S[0]
count = 1
for i in range(1,len(S)):
    if(S[i] == curr):
        count += 1
    else:
        things.append((count,int(curr)))
        count = 1
        curr = S[i]
things.append((count,int(curr)))
print(" ".join(str(i) for i in things))