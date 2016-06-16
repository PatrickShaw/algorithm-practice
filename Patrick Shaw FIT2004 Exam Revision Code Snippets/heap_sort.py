from heap import *


def max_heap_sort(a_list):
    heap = MaxHeapArray(a_list)
    sorted_list = [heap.pop_top() for _ in range(len(a_list))]
    return sorted_list


if __name__ == "__main__":
    print(max_heap_sort([123, 13123, 13122, 2, 21, 11, 1, 1, -1, 21, 2131, 12, 22, 21, 1]))
