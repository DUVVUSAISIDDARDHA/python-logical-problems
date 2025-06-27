
first_name = input("enter first name:")
last_name = input("enter last name:")
result = ""
for i in range(len(last_name)):
    result = result + last_name[i]
result = result + " "
for i in range(len(first_name)):
    result = result + first_name[i]  
print(result)     
