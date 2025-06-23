def cal():
    list = [1,2,3,4]
    
    new_list = []
    mul = 1
    for i in range(len(list)):
           mul = mul * list[i]
    for i in range(len(list)):
           new_list.append(mul//list[i])
         
         
         
    print(new_list)   

cal()        



          