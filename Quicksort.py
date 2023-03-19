def quicksort_algorithm(array_input):

    if len(array_input) <= 1:
        return array_input

    else:
        pivot = array_input[0]
        left = []
        right = []
        
        for i in range(1, len(array_input)):
            if array_input[i] < pivot:
                left.append(array_input[i])

            else:
                right.append(array_input[i])
                
        return quicksort_algorithm(left) + [pivot] + quicksort_algorithm(right)
