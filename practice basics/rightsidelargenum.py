arr = [4, 5, 2, 10]
new_list = []

for i in range(len(arr)):
    if i == len(arr) - 1:
        new_list.append(-1)  
    else:
        max_right = arr[i + 1] 
        for j in range(i + 1, len(arr)):
            if arr[j] > max_right:
                max_right = arr[j]
        new_list.append(max_right)

print(new_list)
           