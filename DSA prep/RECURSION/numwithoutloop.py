def printnum(n):
    if n == 0:
        return
    printnum(n -1)
    print(n, end=" ")
n = int(input("enter a number:"))
printnum(n)    