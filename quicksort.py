def quicksort_algorithm(input_array):
    if len(input_array) <= 1:
        return input_array, [input_array]

    else:
        pivot_element = input_array[0]
        left_array = []
        right_array = []
        
        for i in range(1, len(input_array)):
            if input_array[i] < pivot_element:
                left_array.append(input_array[i])

            else:
                right_array.append(input_array[i])
        
        sorted_left_array, left_intermediate_states = quicksort_algorithm(left_array)
        sorted_right_array, right_intermediate_states = quicksort_algorithm(right_array)
        
        intermediate_states = left_intermediate_states + [sorted_left_array + [pivot_element] + sorted_right_array] + right_intermediate_states
        
        return sorted_left_array + [pivot_element] + sorted_right_array, intermediate_states


''' Test code 
unsorted_list = [3, 1, 4, 2, 6, 5]
sorted_list, all_intermediate_states = quicksort_algorithm(unsorted_list)
print("Sorted list:", sorted_list)
print("All intermediate states:", all_intermediate_states)
'''
