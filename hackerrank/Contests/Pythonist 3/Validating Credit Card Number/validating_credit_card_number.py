n = int(input())
for j in range(n):
    text = input()
    noDigits = 0
    noConseqDigits = 0
    noHyphonCount = 0
    noHyphonConseqCount = 0
    invalid = False
    if  not (text[0] == '4' or text[0] == '5' or text[0] == '6'):
        invalid = True
    noConseqNumber = 0
    stripText = ""
    for i in range(len(text)):
        if text[i].isdigit():
            noDigits += 1
            noConseqDigits += 1
            noHyphonConseqCount = 0
            stripText += text[i]
        elif text[i] == "-":
            noHyphonConseqCount += 1
            noHyphonCount += 1
            if noConseqDigits !=  4:
                invalid = True
                break
            noConseqDigits = 0
        else:
            invalid = True
            break
        if noHyphonConseqCount > 1:
            invalid = True
            break
    #print(noConseqDigits)
    if not text[len(text) - 1].isdigit() or len(stripText) != 16:
        invalid = True
    if (noConseqDigits != 4 and noConseqDigits != 0) and noHyphonCount > 0:
        invalid = True
    for i in range(len(stripText) - 1):
        noConseqNumber += 1
        if stripText[i] != stripText[i+1]:
            if noConseqNumber > 3:
                invalid = True
                break
            noConseqNumber = 0
    if len(stripText) > 2:
        if stripText[len(stripText) - 2] != stripText[len(stripText) - 1]:
            if noConseqNumber > 3:
                invalid = True
    if invalid:
        print("Invalid")
    else:
        print("Valid")
            