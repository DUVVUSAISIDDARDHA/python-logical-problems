
list = [1,1,2,2,3,4]
for i in range(len(list)):
    for j in range(i+1,len(list)-1):
        if list[i] == list[j]:
            list.pop(j)
print(list)            
