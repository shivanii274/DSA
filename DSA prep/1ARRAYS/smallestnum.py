n = int(input("enter the element of an array:"))
arr = []
for i in range(n):
    num = int(input("enter the element :"))
    arr.append(num)
smallest = arr[0]
for i in range(1 ,n):
    if arr[i] < smallest:
        smallest = arr[i]
print("smallest element:",smallest)    
