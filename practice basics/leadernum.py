
list = [16,17,4,3,5,2]
new_list = []
for i in range(len(list)):
    is_leader = True
    for j in range(i + 1,len(list)):
        if list[i]<list[j]:
            is_leader = False
            break
    if is_leader:
        new_list.append(list[i])

print(new_list)
    
   