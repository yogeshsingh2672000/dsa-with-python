# time complexity is O(logn)
def binarySearch(arr, target):
    L = 0
    R = len(arr)-1

    while L<=R:
        M = (L+R)//2
        if target < M:
            R = M-1
        elif target > M:
            L = M+1
        else:
            return arr.index(M)
    return -1

print(binarySearch([1, 2, 3, 4, 5, 6], 7))