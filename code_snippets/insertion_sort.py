def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        for j in range(i - 1, -1, -1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
            else:
                break