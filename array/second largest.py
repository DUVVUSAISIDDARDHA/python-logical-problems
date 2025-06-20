arr =[1,34,56,35,21,34]
unique = list(set(arr))
unique.sort()

if len(arr)>=2:
    print("second largest element is:",unique[-2])
else:
    print("only one element present in list")  

# without inbuilt

arr1 =[1,34,57,45,36] 
first = -1
second = -1
for i in range(len(arr1)):
    if arr1[i] > first:
        second = first
        first = arr1[i]
    elif arr1[i] > second and arr1[i] != first:
       second = arr1[i] 
if second == -1:
    print("No second largest element")
else:
    print("Second largest element is:", second)        
