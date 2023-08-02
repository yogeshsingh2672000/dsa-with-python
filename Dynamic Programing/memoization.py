# Q. Find Febonacci 

# 1-Dimension (top->bottom approach)
def memoizationTB(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = memoizationTB(n - 1, cache) + memoizationTB(n - 2, cache)
    return cache[n]

# 1-Dimension (bottom->top approach)
def memoizationBT(n):
    if n < 2:
        return n
    
    dp = [0, 1] # f(0)=0, f(1)=1
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1]

print(memoizationTB(12, {}))
print(memoizationBT(12))