def selection_sort(a_list):
    for i in range(len(a_list)-1):
        min_index = i
        for j in range(i + 1, len(a_list)):
            if a_list[min_index] > a_list[j]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
