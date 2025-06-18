
arr = [1,2,3,4,5,6,78,9,5]
even = 0
odd = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
      even = even+ 1
    else:
       odd = odd +1

print("even count is",even)
print("odd count is",odd)            