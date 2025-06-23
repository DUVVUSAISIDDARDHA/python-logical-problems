lst = [16, 17, 4, 3, 5, 2]
new_list = []

for i in range(len(lst)):
    if i == len(lst) - 1:
        new_list.append(-1)  # last element
    else:
        greatest = lst[i + 1]  # start from next element
        for j in range(i + 1, len(lst)):
            if lst[j] > greatest:
                greatest = lst[j]
        new_list.append(greatest)

print(new_list)
