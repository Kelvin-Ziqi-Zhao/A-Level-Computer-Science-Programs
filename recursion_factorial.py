def factorial(n):
    if n == 1:
        Result = 1
    else:
        Result = n*factorial(n-1)
    print(Result)
    return Result
print(factorial(10))