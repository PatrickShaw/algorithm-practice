import numbers
from selection_sort import *
from insertion_sort import *
from quick_sort import *
from merge_sort import *
from binary_radix_sort import *

class StabilityUnit:
    def __init__(self, value, stability_value):
        self.value = value
        self.stability_value = stability_value

    def __lt__(self, other):
        if isinstance(other, numbers.Number):
            return self.value < other
        return self.value < other.value

    def __le__(self, other):
        if isinstance(other, numbers.Number):
            return self.value <= other
        return self.value <= other.value

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return self.value == other
        return self.value == other.value

    def __ne__(self, other):
        if isinstance(other, numbers.Number):
            return self.value != other
        return self.value != other.value

    def __gt__(self, other):
        if isinstance(other, numbers.Number):
            return self.value > other
        return self.value > other.value

    def __ge__(self, other):
        if isinstance(other, numbers.Number):
            return self.value >= other
        return self.value >= other.value

    def __lshift__(self, other):
        return StabilityUnit(self.value << other, self.stability_value)

    def __rshift__(self, other):
        return StabilityUnit(self.value >> other, self.stability_value)

    def __abs__(self):
        return StabilityUnit(abs(self.value), self.stability_value)

    def __mod__(self, other):
        return StabilityUnit(self.value % other, self.stability_value)

    def __str__(self):
        return str(self.value) + str(self.stability_value)

def print_list(a_list):
    print("\t\t".join([str(x) for x in a_list]))

print("Original list: ")
original = [StabilityUnit(1, "a"),
            StabilityUnit(3, "a"),
            StabilityUnit(5, "a"),
            StabilityUnit(6, "b"),
            StabilityUnit(1, "b"),
            StabilityUnit(1, "c"),
            StabilityUnit(1, "d"),
            StabilityUnit(44, "a"),
            StabilityUnit(6, "b"),
            StabilityUnit(4, "a"),
            StabilityUnit(234, "a"),
            StabilityUnit(234, "b"),
            StabilityUnit(24, "a"),
            StabilityUnit(11, "a"),
            StabilityUnit(1, "e"),
            StabilityUnit(1, "f"),
            StabilityUnit(1, "g"),
            StabilityUnit(102, "a"),
            StabilityUnit(10, "a"),
            StabilityUnit(10213131, "a"),
            StabilityUnit(1201, "a"),

            StabilityUnit(102, "b"),
            StabilityUnit(10, "b"),
            StabilityUnit(10213131, "b"),
            StabilityUnit(1201, "b"),

            StabilityUnit(102, "c"),
            StabilityUnit(10, "c"),
            StabilityUnit(10213131, "c"),
            StabilityUnit(1201, "c"),

            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(-1, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),

            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(9999, "a"),
            StabilityUnit(99, "a"),
            StabilityUnit(999, "a"),
            StabilityUnit(999, "a"),
            ]

def test_properties(correct, tested):
    is_stable = True
    for i in range(len(correct)):
        if correct[i] != tested[i]:
            print("INCORRECT")
            return
        if correct[i].stability_value != tested[i].stability_value:
            is_stable = False
    print("Correct, " + ("stable" if is_stable else "unstable"))

import time
print_list(original)
print(len(original))
print()
print("Correctly sorted: ")
a = time.time()
sorted = sorted(original)
b = time.time()
print(b - a)
print_list(sorted)
print()

print("Selection sorted: ")
selection_sorted_list = list(original)
a = time.time()
selection_sort(selection_sorted_list)
b = time.time()
print(b - a)
print_list(selection_sorted_list)
test_properties(sorted, selection_sorted_list)
print()

print("Insertion sorted: ")
insertion_sorted_list = list(original)
a = time.time()
insertion_sort(insertion_sorted_list)
b = time.time()
print(b - a)
print_list(insertion_sorted_list)
test_properties(sorted, insertion_sorted_list)
print()

print('Radix sorted: ')
binary_radix_sorted_list = list(original)
a = time.time()
binary_radix_sorted_list = binary_radix_sort(binary_radix_sorted_list)
b = time.time()
print(b - a)
print_list(binary_radix_sorted_list)
test_properties(sorted, binary_radix_sorted_list)
print()

print("Merge sorted: ")
merge_sorted_list = list(original)
a = time.time()
merge_sorted_list = merge_sort(merge_sorted_list)
b = time.time()
print(b - a)
print_list(merge_sorted_list)
test_properties(sorted, merge_sorted_list)
print()

print("Quick sorted: ")
quick_sorted_list = list(original)
a = time.time()
quick_sort(quick_sorted_list)
b = time.time()
print(b - a)
print_list(quick_sorted_list)
test_properties(sorted, merge_sorted_list)