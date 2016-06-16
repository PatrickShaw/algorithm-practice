def burrows_wheeler_transform(a_string):
    rotations = [a_string[x:] + a_string[:x] for x in range(len(a_string))]
    return "".join(x[-1] for x in sorted(rotations))


def decode_burrows_wheeler_transform(a_string):
    strings = [""]*len(a_string)
    for i in range(len(a_string)):
        strings = sorted(a_string[j] + strings[j] for j in range(len(strings)))
    return strings[-1][1:] + strings[-1][0]
bwt = burrows_wheeler_transform("^banana|")
print(bwt)
print(decode_burrows_wheeler_transform(bwt))