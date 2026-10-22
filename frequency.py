n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter element to find frequency: "))

count = 0

for i in range(n):
    if arr[i] == target:
        count += 1

print("Frequency:", count)