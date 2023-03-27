def merge_sort(arr):
    def merge(left, right):
        merged_list = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1
        merged_list += left[i:]
        merged_list += right[j:]
        return merged_list

    if len(arr) <= 1:
        return arr, [arr]

    else:
        mid = len(arr) // 2
        left, left_merges = merge_sort(arr[:mid])
        right, right_merges = merge_sort(arr[mid:])
        sorted_arr = merge(left, right)
        merges = []
        for l in left_merges:
            for r in right_merges:
                merges.append(merge(l, r))
        return sorted_arr, [arr] + merges + [sorted_arr]

''' Test code
unsorted_list = [3, 1, 4, 2, 6, 5]
sorted_list, all_merges = merge_sort(unsorted_list)
print("Sorted list:", sorted_list)
print("All merges:", all_merges)
'''
