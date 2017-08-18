s = input()
s = s[0].upper() + s[1:]
for i in range(1,len(s)-1):
    if(s[i] == ' '):
        s = s[:i+1]+ s[i+1].upper()+ s[i + 2:]
print(s)