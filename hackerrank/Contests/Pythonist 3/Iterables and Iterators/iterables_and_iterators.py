def calc(thing,combos,curr,i, turns ):
    curr.append(thing[i])
    
    if len(curr) >= turns or i >= len(thing):
        if len(curr) >= turns:
            combos.append(curr)
        return
    for j in range(i+1,len(thing)):
        calc(thing,combos,list(curr),j, turns)
    
n = int(input())
thing = input().replace(" ","" )
k = int(input())
total = []
for i in range(n):
    calc(thing,total,[],i,k)
count = 0
for i in range(len(total)):
    found = False
    for j in range(len(total[i])):
        if total[i][j] == 'a':
            found = True
    if found:
        count += 1
print(round(float(count) / float(len(total)),3))