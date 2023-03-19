def quicksort_algorithm(arrayInput):

    if len(arrayInput) <= 1:
        return arrayInput

    else:
        pivot = arrayInput[0]
        left = []
        right = []
        
        for i in range(1, len(arrayInput)):
            if arrayInput[i] < pivot:
                left.append(arrayInput[i])

            else:
                right.append(arrayInput[i])
                
        return quicksort_algorithm(left) + [pivot] + quicksort_algorithm(right)
