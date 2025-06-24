
list = [0,0,0,0,1,2,0,3,0,4]
for i in range(len(list)):
    if list[i] == 0:
        list.remove(0)
        list.append(0)
print(list)        