

def binary_search(sorted_list, value):
    start_index, end_index = 0, len(sorted_list) - 1

    while start_index <= end_index:
        midpoint_index = start_index + (end_index - start_index) // 2
        midpoint_value = sorted_list[midpoint_index]

        # Found our value
        if midpoint_value == value:
            return midpoint_index

        # Search items to the right
        elif midpoint_value < value:
            start_index = midpoint_index + 1

        # Search items to the left
        elif midpoint_value > value:
            end_index = midpoint_index - 1

    return None


s_list = [1, 3, 4, 6, 7, 8, 9]
v = 7

result = binary_search(s_list, v)

if result is None:
    print("Did not find result")
else:
    print("Found {0} at index {1}".format(v, result))
