import time


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    mid = len(a_list) // 2
    p1 = a_list[mid:]
    p2 = a_list[:mid]
    p1 = merge_sort(p1)
    p2 = merge_sort(p2)
    i = 0
    j = 0
    merged_list = [None] * (len(p1) + len(p2))
    while i < len(p1) and j < len(p2):
        if p1[i] < p2[j]:
            merged_list[i + j] = p1[i]
            i += 1
        else:
            merged_list[i + j] = p2[j]
            j += 1
    while i < len(p1):
        merged_list[i + j] = p1[i]
        i += 1
    while j < len(p2):
        merged_list[i + j] = p2[j]
        j += 1
    return merged_list

a = time.time()
print(merge_sort([1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1, 2, 3, 4, 5, 1, 2, 24, 1, 2, 21, 1]))
b = time.time()
print(b - a)