import sys

test_array = [20, 21, 12, 11, 13, 5, 6]
sorted_test_array = sorted(test_array)


def insertion_helper(array, some_previous_index, current_value):
    # Sort by copying elements greater than current value, but before it in the list, up by 1 (break at index = -1)
    while some_previous_index >= 0 and current_value < array[some_previous_index]:
        array[some_previous_index + 1] = array[some_previous_index]  # Copy Element to Prev_Index + 1
        some_previous_index -= 1

    array[some_previous_index + 1] = current_value
    return array


def insertion_sort(array, recursive=False, n=sys.maxsize):
    if len(array) <= 1 or n <= 1:
        return array

    sorted_array = array.copy()  # Copy so we don't alter original

    if recursive:
        num_elems = len(sorted_array) if n == sys.maxsize else n
        sorted_array = insertion_sort(sorted_array, recursive=True,  n=num_elems - 1)
        current_value = sorted_array[num_elems - 1]
        some_previous_index = num_elems - 2

        return insertion_helper(sorted_array, some_previous_index, current_value)

    else:
        for current_index in range(1, len(sorted_array)):  # Start at 2nd element (index = 1) and proceed from there.
            current_value = sorted_array[current_index]
            some_previous_index = current_index - 1
            sorted_array = insertion_helper(sorted_array, some_previous_index, current_value)

        return sorted_array


