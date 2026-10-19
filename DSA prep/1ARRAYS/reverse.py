n = int(input("enter the element of the array:"))
arr = list(map(int, input("enterr the elements in an array:").split()))
k = int(input("enterr k:"))

for i in range(0, n, k):
    arr[i:i+k] = arr[i:i+k][::-1]
print("reverse array:",arr)    
