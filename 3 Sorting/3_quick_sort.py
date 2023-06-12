def quickSort(arr, start, end):
    # simple condition for array not to go out of bound
    if (end-start+1 <= 1):
        return
    
    pivot = arr[end]
    left = start

    # swaping start 
    for i in range(start, end):
        if (arr[i] < pivot):
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    
    # last swap for putting the pivot in the actual sorted position
    arr[end] = arr[left]
    arr[left] = pivot

    # sorting left side
    quickSort(arr, start, left-1)
    # sorting right side
    quickSort(arr, left+1, end)

    return arr

print(quickSort([2, 4, 3, 1, 6], 0, 4))