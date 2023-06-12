# Worst time complexity O(n^2)
# Best time complexity O(n)

def insertionSort(arr):
    for i in range(len(arr)):
        j = i-1
        while (j>=0 and arr[j+1] < arr[j]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    print(arr)
    return arr

insertionSort([2, 4, 3, 1, 6])