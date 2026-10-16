# find min and max values.
arr = list(map(int, input("Enter the elments of the array:").split()))
if len(arr) == 0:
    print("array is not empty")
else:
    min = arr[0]
    max = arr[0]
    for num in arr:
        if num < min :
            min = num
        if num > max:
                max = num
    print("Minimum element:",min)
    print("maximum element:",max)
    print("output :",[min, max])     
