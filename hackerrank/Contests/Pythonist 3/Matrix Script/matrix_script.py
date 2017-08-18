import re
mn = input().split()
rows = int(mn[0])
cols = int(mn[1])
strings = []
for i in range(rows):
    strings.append(input())
result = ""
symbols = ""
x = 0
y = 0
try:
    while (not strings[(rows - 1) - y][(cols - 1) - x].isalnum()) and (not (x >= cols or y >= rows)):
        symbols += strings[(rows - 1) - y][(cols - 1) -x]
        y += 1
        y %= rows
        x += y == 0
except:
    pass
while not (x >= cols or y >= rows):
    result += strings[(rows - 1) - y][(cols - 1) -x]
    y += 1
    y %= rows
    x += y == 0
x = 0
y = 0
start = ""
try:
    while (not (strings[y][x].isalnum())) and (not (x >= cols or y >= rows)):
        start += strings[y][x]
        y+=1
        y%=rows
        x+=y == 0
except:
    pass
start = start[::-1]
result = result[::-1]
symbols = symbols[::-1]
while len(result) == len(symbols):
    print(symbols)
    exit
result = re.findall(r"[\w']+", result)
print(start+" ".join(result) + symbols)