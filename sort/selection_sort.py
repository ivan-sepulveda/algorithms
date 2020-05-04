import sys

test_array = [20, 21, 12, 11, 13, 5, 6]
sorted_test_array = sorted(test_array)


def selection_helper(sorted_array, index_min_unsorted_elem, index_next_unsorted_elem):
    return index_next_unsorted_elem \
        if sorted_array[index_min_unsorted_elem] > sorted_array[index_next_unsorted_elem]\
        else index_min_unsorted_elem


def min_index(sorted_array, index_next_unsorted_elem, j):
    if index_next_unsorted_elem == j:
        return index_next_unsorted_elem

    index_min_unsorted_elem = min_index(sorted_array, index_next_unsorted_elem + 1, j)

    return selection_helper(sorted_array, index_min_unsorted_elem, index_next_unsorted_elem)


def selection_sort(array, recursive=True, n=sys.maxsize, index_min_unsorted_elem=0):
    array_length, sorted_array = len(array), array.copy()

    if array_length <= 1 or n == 0 or index_min_unsorted_elem == n:
        return array

    if recursive:
        num_elems = len(sorted_array) if n == sys.maxsize else n

        k = min_index(sorted_array, index_min_unsorted_elem, num_elems - 1)
        sorted_array[k], sorted_array[index_min_unsorted_elem] = sorted_array[index_min_unsorted_elem], sorted_array[k]
        sorted_array = selection_sort(sorted_array, True, num_elems, index_min_unsorted_elem + 1)

    else:

        for k in range(array_length):
            index_min_unsorted_elem = k

            for index_next_unsorted_elem in range(k+1, array_length):
                index_min_unsorted_elem = selection_helper(sorted_array, index_min_unsorted_elem, index_next_unsorted_elem)

            sorted_array[k], sorted_array[index_min_unsorted_elem] = sorted_array[index_min_unsorted_elem], sorted_array[k]

    return sorted_array


