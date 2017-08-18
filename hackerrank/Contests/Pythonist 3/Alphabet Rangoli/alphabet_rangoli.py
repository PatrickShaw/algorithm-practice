def thing(curI,maxI):
    stringI = letters[maxI - curI]
    for i in range(curI - 1, -1, -1):
        stringI += "-"+letters[maxI - i]
        stringI = letters[maxI - i]+"-" + stringI
    while len(stringI) < 4*N-3:
        stringI += "-"
        stringI = "-" + stringI
    return stringI
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
N = int(input())
for i in range(N-1):
    print(thing(i,N-1))
print(thing(N-1,N-1))
for i in range(N-2,-1,-1):
    print(thing(i,N-1))