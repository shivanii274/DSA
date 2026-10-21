n = int(input("enter the number of elements of the array:"))

arr = list(map(int, input("enter the elements int the array:").split()))

Target = int(input(" enter the target element in the array:"))
found = False
for i in range(n):
    if arr[i] == Target:
        print("found the target element at index:", i)
        found = True
        break
if not found:
    print("target element not found in the array")  