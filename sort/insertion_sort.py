
test_array = [20, 21, 12, 11, 13, 5, 6]
sorted_test_array = sorted(test_array)


def insertion_sort(array):
    sorted_array = array.copy()  # Copy so we don't alter original

    for current_index in range(1, len(sorted_array)):  # Start at 2nd element (index = 1) and proceed from there.

        current_value = sorted_array[current_index]
        some_previous_index = current_index - 1

        # Sort by copying elements greater than current value, but before it in the list, up by 1 (break at index = -1)

        while some_previous_index >= 0 and current_value < sorted_array[some_previous_index]:
            sorted_array[some_previous_index+1] = sorted_array[some_previous_index]  # Copy Element to Prev_Index + 1
            some_previous_index -= 1
        sorted_array[some_previous_index+1] = current_value

    return sorted_array


print(insertion_sort(test_array) == sorted_test_array)


