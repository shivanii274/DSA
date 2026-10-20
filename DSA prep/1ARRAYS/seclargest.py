n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))

largest = arr[0]
second_largest = None

for i in range(1, n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
        second_largest = arr[i]

if second_largest is None:
    print("Second largest distinct element does not exist")
else:
    print("Second largest element:", second_largest)