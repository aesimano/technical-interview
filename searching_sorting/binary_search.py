"""
Binary Search

Efficiency
    O(logn)

"""

def binary_search(input_array, value):
    """Your code goes here."""
    head = 0
    end = len(input_array) - 1
    index = int((end - head)/2)

    while True:
        if end < head:
            return -1

        if input_array[index] == value:
            return index
        elif value > input_array[index]:
            head = index + 1
        elif value < input_array[index]:
            end = index - 1
        index = head + int((end - head)/2)

test_list = [1,3,9,11,15,19,29]
# test_list = [1,3,9,11,15,19]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, 29)