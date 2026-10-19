n = int(input("enter the elements of the array:"))
arr = list(map(int, input("enter the elemnts in the array:").split()))

even = 0
odd = 0

for i in range(n):
    if arr[i]%2 == 0:
        even += 1
    else:
        odd += 1

print("even num", even)
print("odd num:", odd)
