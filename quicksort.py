def quicksort_algorithm(input_array):

    if len(input_array) <= 1:
        return input_array

    else:
        pivot_element = input_array[0]
        left_array = []
        right_array = []
        
        for i in range(1, len(input_array)):
            if input_array[i] < pivot_element:
                left_array.append(input_array[i])

            else:
                right_array.append(input_array[i])
                
        return quicksort_algorithm(left_array) + [pivot_element] + quicksort_algorithm(right_array)
