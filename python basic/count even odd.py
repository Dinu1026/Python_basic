# creating an empty list 
lst = []

# number of elemetns as input 
n = int(input("Enter number of elements : "))

# iterating till the range 
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst) 
def count(lst):
     even=0
     odd=0
     for i in lst:
         if i%2==0:
             even+=1
         else:
            odd+=1
     return even,odd

even,odd = count(lst)
print("even:{},odd:{}".format(even,odd))
