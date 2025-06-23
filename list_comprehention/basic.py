
list = [1,2,3,4]
sqrs = [p*p for p in list]
print(sqrs)

# if 
list = [1,2,3,4]
evens = [x for x in list if x % 2== 0]
print(evens)

#if else
list = [1,2,3,4,5]
e_o = ["even" if x %2 ==0 else "odd" for x in list]
print(e_o)


