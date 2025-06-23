
list = [1,2,3,1,2,3,3,2,5,6,7]
new_list = []
for i in range(len(list)):
    if list[i] not in new_list:
        count = 1        
        for j in range(i+1,len(list)):
            if list[i]==list[j]:
              count = count + 1
        
        print(f"{list[i]} -> {count}") 
        new_list.append(list[i])       
