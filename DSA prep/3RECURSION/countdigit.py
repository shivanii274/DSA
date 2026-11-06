def countDigits(n):
    if n == 0:
        return 1

    if n < 10:
        return 1

    return 1 + countDigits(n // 10)
n = int(input("Enter a number: "))
print(countDigits(n))