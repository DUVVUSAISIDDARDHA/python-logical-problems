list = [1,2,2,3,1]
dict ={}
for i in range(len(list)):
    key = list[i]
    if list[i] not in dict:
        count = 1
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                count = count + 1
        dict[key] = count        

print(dict)
 
    
    