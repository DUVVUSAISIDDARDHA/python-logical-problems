arr = [1,3,4,5,6,7,8,6]
target = 8
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("element found at index ",i)
        found = True
        break
if not found:
    print("element not existed")    

         