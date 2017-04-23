from collections import defaultdict


def can_make_ransom_note(magazine, ransom):
    """
    Checks if you can make a ransom note out of a magazine.
    :param magazine:
        The array of words in the magazine
    :param ransom:
        The array of words in the ransom note
    :return:
        True: You can make a ransom note out of the magazine
        False: You cannot
    """
    # We need a default dictionary so that we don't have to pre-assign 0s to each key
    word_count_difference = defaultdict(lambda: 0)
    """Represents the number of words left in the magazine"""
    # Grab the counts of each word in the magazine
    for word in magazine:
        word_count_difference[word] += 1
    # Take a word
    for word in ransom:
        if word_count_difference[word] <= 0:
            # We don't any of this word left in the remaining magazine words collection.
            return False
        else:
            # Use the word in the ransom note, 1 word less to use from te magazine
            word_count_difference[word] -= 1
    # If we got here then we were successful in our attempt to make the ransom note
    return True


input()  # ignore m and n
answer = can_make_ransom_note(input().split(' '), input().split(' '))
if answer:
    print("Yes")
else:
    print("No")
