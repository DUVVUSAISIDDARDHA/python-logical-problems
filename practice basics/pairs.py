sum = 6
list = [1,2,3,4,5]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j] == sum:
            print(f"({list[i]},{list[j]})")
