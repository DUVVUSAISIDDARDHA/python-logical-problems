
list = [1,2,3,4]
new_list = []
for i in range(len(list)):
    mul = 1
    for j in range(len(list)):
        if i != j:
            mul = mul * list[j]
    new_list.append(mul)

print(new_list)            
