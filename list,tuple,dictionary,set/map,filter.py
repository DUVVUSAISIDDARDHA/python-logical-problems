#map()
list1= [1,2,3,4,5]
square =list( map(lambda x: x * x ,list1))
print(square)
#filter()
a = [1,2,3,4,5]
evens = list(filter(lambda x:  x %2 ==0 ,a))
print(evens)