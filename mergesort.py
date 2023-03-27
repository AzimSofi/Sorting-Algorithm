def mergesort(array_input):

    if len(array_input) <= 1:
        return array_input

    else:
        middle_index = len(array_input) // 2
        left_array = mergesort(array_input[:middle_index])
        right_array = mergesort(array_input[middle_index:])
        merged_array = []
        i, j = 0, 0

        while i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[j]:
                merged_array.append(left_array[i])
                i += 1

            else:
                merged_array.append(right_array[j])
                j += 1

        merged_array += left_array[i:]
        merged_array += right_array[j:]
        
        # return intermediate state of merged_array
        return merged_array, left_array, right_array
