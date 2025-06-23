
list = [0, -3, 5, -2, 1, 0, -4]
count1 = 0
count2 = 0
count3 = 0
for val in list:
    if val == 0 :
        count1 =count1+1
    elif (val / 1) < 0:
        count2 = count2+1
    elif (val / 1) > 0:
        count3 = count3+1
print("number of zeroes:",count1)         
print("number of negitive:",count2)   
print("number of positive:",count3)   