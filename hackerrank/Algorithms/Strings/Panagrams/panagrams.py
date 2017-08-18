s = input()
s = s.lower()
isUsed = [0]*133
for i in range(len(s)):
    isUsed[ord(s[i])] += 1
for i in range(97,122):
    if(isUsed[i] <= 0):
        print("not pangram")
        sys.exit()
print("pangram")