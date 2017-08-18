T = int(input())
for i in range(T):
    s = input()
    r = list(reversed(s))
    notFunny = False
    for q in range(1,len(s)):
        if (abs(ord(s[q]) - ord(s[q-1])) != abs(ord(r[q]) - ord(r[q - 1]))):
            print("Not Funny")
            notFunny = True
            break
    if notFunny == False:
        print("Funny")
            