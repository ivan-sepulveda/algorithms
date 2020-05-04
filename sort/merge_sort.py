
test_array = [38, 27, 43, 3, 9, 82, 10]
sorted_test_array = sorted(test_array)


def merge_sort(array, alternative=True):
    array_length = len(array)
    sorted_array = array.copy()
    if array_length <= 1:
        return sorted_array
    elif alternative:
        median_index = array_length // 2 - (1 if array_length % 2 == 0 else 0)
        left, right = array[:median_index + 1], array[median_index + 1:]

        left = merge_sort(left)
        right = merge_sort(right)

        sorted_array.clear()

        while left and right:
            if left[0] <= right[0]:
                sorted_array.append(left[0])
                left.pop(0)
            else:
                sorted_array.append(right[0])
                right.pop(0)

        for value in left + right:
            sorted_array.append(value)

        return sorted_array
    else:
        median_index = array_length // 2 - (1 if array_length % 2 == 0 else 0)
        left, right = array[:median_index + 1], array[median_index + 1:]

        left = merge_sort(left, alternative=False)
        right = merge_sort(right, alternative=False)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                sorted_array[k] = left[i]
                i, k = i + 1, k + 1

            else:
                sorted_array[k] = right[j]
                j, k = j + 1, k + 1

        while i < len(left):
            sorted_array[k] = left[i]
            i, k = i+1, k+1

        while j < len(right):
            sorted_array[k] = right[j]
            j, k = j+1, k+1

        return sorted_array



