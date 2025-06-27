list = [1,1,2,2,3,4]
new_list =[]
for i in range(len(list)):
    for j in range(i+1,len(list)-1):
        if list[i] == list[j]:
           list.append(i)
print(list)


list = [1,1,2,2,3,4]
new_list = set(list)
print(new_list)
print(len(new_list))


list = [1, 1, 2, 2, 3, 4]
new_list =[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
                new_list.append(list[i])
for i in range(len(list)):
     if list[i] not in new_list:
          new_list.append(list[i])
          

print(new_list) 
print(len(new_list))  
