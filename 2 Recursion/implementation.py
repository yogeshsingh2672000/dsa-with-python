# factorial -- one branch recursion -- O(n)
def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n-1)

print(factorial(5))

# fabonacci -- two branch recursion -- O(2^n)
def fabonacci(n):
    if (n <= 1):
        return n
    return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(5))