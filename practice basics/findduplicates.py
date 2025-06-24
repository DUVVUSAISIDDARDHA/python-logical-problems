
list =[4, 4,3,3,2,2,1]
new_list = []
for i in range(len(list)):
    count = 1
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            count = count + 1
            if count > 1:
                new_list.append(list[i])
print(new_list)                

