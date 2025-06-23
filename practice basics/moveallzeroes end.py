
list = [1, 0, 2, 0, 3, 4]
i =0
n = len(list)      
while i<n:
    if list[i]==0:
        list.pop(i)
        list.append(0)
        n = n-1
    else:
        i = i+1
print(list)        