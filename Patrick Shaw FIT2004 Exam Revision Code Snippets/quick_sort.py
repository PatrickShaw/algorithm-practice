def quick_sort(a_list):
    """
        First index in sub list is always being picked as the pivot
    """
    quick_sort_sub_list(a_list, 0, len(a_list) - 1)


def quick_sort_sub_list(a_list, min_index, max_index):
    if min_index >= max_index:
        return
    pivot_index = partition(a_list, min_index, max_index)
    quick_sort_sub_list(a_list, min_index, pivot_index - 1)
    quick_sort_sub_list(a_list, pivot_index + 1, max_index)


def partition(a_list, min, max):
    pivot_value = a_list[max]
    i = min
    for j in range(min, max):
        if a_list[j] <= pivot_value:
            a_list[j], a_list[i] = a_list[i], a_list[j]
            i += 1
    a_list[i], a_list[max] = a_list[max], a_list[i]
    return i


if __name__ == "__main__":
    test_list = [1, 32, 4, 41, 2141231, 31, 12, 22, 2, 4, 5, 6, 7, 3, 3, 2, 21, 234, 2, 2]
    quick_sort(test_list)
    print(test_list)
