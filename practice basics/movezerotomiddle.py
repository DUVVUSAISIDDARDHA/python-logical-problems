list = [1, 0, 2, 0, 3, 4]
nonzero = []
count = 0
for i in range(len(list)):
    if list[i] == 0:
        count = count + 1
    else:
        nonzero.append(list[i])
mid =  len(nonzero) // 2 
res =[]   
for i in range(mid):
    res.append(nonzero[i])
for i in range(count):
    res.append(0)
for i in range(mid,len(nonzero)):
    res.append(nonzero[i])
print(res)




     