def merge_sort(arr):
    if len(arr) > 1:  # Base case: 1
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = 0  # Left array index
        j = 0  # Right array index
        k = 0  # Merged array index

        # Scenario 1 (Comparison between both arrays)
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Scenario 2 (Leftovers in left array)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Scenario 3 (Leftovers in right array)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr_test1 = [93, 5, 343, 5435, 5, 25, 45, 80, 32]
    merge_sort(arr_test1)
    print(arr_test1)
