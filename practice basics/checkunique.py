
list = [1,2,3,4,5]
is_unique = True
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]== list[j]:
         is_unique = False
         break
    if not is_unique:
       break
if is_unique  ==False:
   print("false")
else:
   print("true")        
