def bucketSort(arr):
    bucket = [0] * 3
    for i in arr:
        bucket[i] += 1

    k = 0
    for i in range(len(bucket)): # 2, 2, 3
        for j in range(bucket[i]):
            arr[k] = i
            k += 1
    return arr


test = [1, 1, 0, 2, 0, 2, 2]
print(bucketSort(test))