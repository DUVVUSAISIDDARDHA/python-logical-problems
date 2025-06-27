
user_input = input("enter number with commas:")
list = []
tuple = ()
for i in range(len(user_input)):
    
    if user_input[i]  !=',':
        list.append(user_input[i])
        
print(list)
for i in range(len(list)):
    tuple = tuple + (list[i],)
print(tuple)    

