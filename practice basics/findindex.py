list = [1,2,3,4,2]
indices = []
for i in range(len(list)):
    if list[i] == 2:
      indices.append(i)
print(indices)