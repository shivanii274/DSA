n = int(input("enter number of element "))
arr = list(map(int,input("enter array elements:").split()))
positive = 0
negative = 0
true = 0
for i in range(n):
    if arr[i] > 0:
        positive += 1
    elif arr[i] < 0:
        negative += 1
    else:
        true += 1
print("positive:", positive)
print("negative:", negative)
print("zero:", true)