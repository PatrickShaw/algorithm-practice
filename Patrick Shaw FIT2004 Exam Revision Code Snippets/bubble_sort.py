def bubble_sort(a_list):
    for i in range(len(a_list)):
        swapped = False
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True
        if not swapped:
            return

if __name__ == "__main__":
    test_list = [123,1,12,2,1212,12313,131,22,22,21,112,1,21,21,1,-1,1212,131,12,1,21,21,122,3123,1,23,23,232,]
    bubble_sort(test_list)
    print(test_list)
