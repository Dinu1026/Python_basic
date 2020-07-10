from array import *
arr= array('i',[])
n = int(input("Enter the length of array"))
for i in range(n):
    x=int(input("enter the ext element of array"))
    arr.append(x)
print(arr)
min = arr[0]
for a in arr:
    if a < min:
        min=a
    arr.append(min)


print(arr)