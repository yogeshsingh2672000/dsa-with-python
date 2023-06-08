# BruteForce: O(n^2)
def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(maxSum, currSum)
    return maxSum


# Kadane's Algo: O(n)
def kadaneAlgo(nums):
    # keeping track of max and current sum
    maxSum = nums[0]
    currSum = 0

    for n in nums:
        currSum = n + max(currSum, 0)
        maxSum = max(currSum, maxSum)
    return maxSum

print(kadaneAlgo([4, -1, 2, -7, 3, 4]))