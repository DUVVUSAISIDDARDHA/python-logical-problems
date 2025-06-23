
list = [1,2,2,3,4,3,5,4,5]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            list.pop(j)
print(list)            
