def number_needed(a, b):
    difference = dict()
    """
    A dictionary with keys represented as the elements in a and b
    and key-values represented as the difference in the number of occurrences for that key
    """
    # +1 for each occurrence of a particular element in a
    for a_element in a:
        difference[a_element] = 1 if a_element not in difference else difference[a_element] + 1
    # -1 for each occurrence of a particular element in b
    for b_element in b:
        difference[b_element] = -1 if b_element not in difference else difference[b_element] - 1
    # All we need to do now is sum up all the difference count for each key in the dictionary
    deletions = 0
    for key_value_pair in difference.items():
        deletions += abs(key_value_pair[1])
    return deletions

a = input().strip()
b = input().strip()

print(number_needed(a, b))