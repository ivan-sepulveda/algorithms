
test_array = [20, 21, 12, 11, 13, 5, 6]
sorted_test_array = sorted(test_array)


def bubble_sort(array):
    sorted_array = array.copy()
    num_elems = len(sorted_array)
    for i in range(num_elems - 1):
        for j in range(0, num_elems - i - 1):
            if sorted_array[j] > sorted_array[j+1]:
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]
    return sorted_array

print(bubble_sort(test_array) == sorted_test_array)