from collections import deque


def binary_radix_sort(a_list):
    max_index = 0
    for i in range(1, len(a_list)):
        if a_list[max_index] < a_list[i]:
            max_index = i
    zero_list = deque()
    one_list = deque()
    for value in a_list:
        if value < 0:
            zero_list.append(value)
        else:
            one_list.append(value)
    max_value = a_list[max_index]
    i = 0
    while max_value > 0:
        original_zero_len = len(zero_list)
        original_one_len = len(one_list)
        for j in range(original_zero_len):
            value = zero_list.popleft()
            if (abs(value) >> i) % 2 == 0:
                zero_list.append(value)
            else:
                one_list.append(value)
        for j in range(original_one_len):
            value = one_list.popleft()
            if (abs(value) >> i) % 2 == 0:
                zero_list.append(value)
            else:
                one_list.append(value)
        max_value >>= 1
        i += 1
    return zero_list + one_list
