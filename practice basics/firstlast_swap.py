
list = [1,2,3,4]
start = 0
end = len(list)-1
temp = list[0]
list[0] = list[end]
list[end] = temp
print(list)
