
list = [1,2,3,4]
new_list = []
for i in range(len(list)):
    sum =0
    for j in range(len(list)):
        if i != j:
            sum = sum + list[j]
    new_list.append(sum)
print(new_list)            
