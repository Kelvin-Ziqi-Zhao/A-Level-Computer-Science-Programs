def PrintDecimal(n):
    print(n%10)
    if n>=10:
        (PrintDecimal(n//10))
    print(n%10)

PrintDecimal(365)