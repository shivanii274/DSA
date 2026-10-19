n = int(input("Enter the number of elements in an array: "))
arr = list(map(int,input("enter the elements of the array:").split()))
smallest = arr[0]

for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element:", smallest)