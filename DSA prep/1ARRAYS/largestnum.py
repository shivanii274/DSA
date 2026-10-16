arr = list(map(int, input("Enter array elements: ").split()))

if len(arr) == 0:
    print("Array cannot be empty")
else:
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    print("Largest element:", largest)
