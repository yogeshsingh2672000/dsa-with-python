def mergeSort(arr):
    # simple condition for array not to go out of bound
    if len(arr) > 1:
    
        middle = len(arr)//2
        Lside = arr[:middle]
        Rside = arr[middle:]

        mergeSort(Lside)
        mergeSort(Rside)

        # i pointer for left side of arr
        # j pointer for left side of arr 
        # k pointer for parent array were sorted element is stored
        i = j = k = 0

        while i < len(Lside) and j < len(Rside):
            if Lside[i] < Rside[j]:
                arr[k] = Lside[i]
                i += 1
            else:
                arr[k] = Rside[j]
                j += 1
            k += 1

        # checking is any element left in Left side of array
        while i < len(Lside):
            arr[k] = Lside[i]
            i += 1

        # checking is any element Right in Left side of array
        while j < len(Rside):
            arr[k] = Rside[j]
            j += 1

    return arr

print(mergeSort([2, 4, 3, 1, 6]))