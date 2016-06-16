def binary_search(a_list, value):
    return binary_search_sub_list(a_list, value, 0, len(a_list) - 1)


def binary_search_sub_list(a_list, value, min, max):
    """
    :return: The index of the value in the container
    """
    if min > max:
        return None
    mid = (min + max) // 2
    searched_value = a_list[mid]
    if value < searched_value:
        return binary_search_sub_list(a_list, value, min, mid - 1)
    elif value > searched_value:
        return binary_search_sub_list(a_list, value, mid + 1, max)
    else:
        return mid


def binary_search_iterative(a_list, value):
    return binary_search_iterative_sub_list(a_list, value, 0, len(a_list) - 1)


def binary_search_iterative_sub_list(a_list, value, min, max):
    while min <= max:
        mid = (min + max) // 2
        searched_value = a_list[mid]
        if value < searched_value:
            max = mid - 1
        elif value > searched_value:
            min = mid + 1
        else:
            return mid
    return None


if __name__ == "__main__":
    a_list = [x for x in range(100)]
    print(a_list)
    while True:
        integer = int(input("Search for a value: "))
        print(binary_search(a_list, integer))
