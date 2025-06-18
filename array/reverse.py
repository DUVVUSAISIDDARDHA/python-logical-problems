arr1 = [1,2,3,4,5]
start =0
end = len(arr1)-1
for i in range(len(arr1)):
    if start < end:
       temp = arr1[start]
       arr1[start] = arr1[end]
       arr1[end] = temp

       start = start +1
       end = end -1
print(arr1)    



# inbuilt
arr = [1,2,3,4,5]
arr.reverse()
print(arr)
