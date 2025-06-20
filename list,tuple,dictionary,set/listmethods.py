
# append() - adds item at the end
a = ["mango","orange",4,6,True,"sai"]
a.append("hemanth")
print(a)

# insert() - at particular position we can add item
b = ["mango","orange",4,6,True,"sai"]
b.insert(1,"rohan")
print(b)

# extend() - add other list to thr existing list
c = ["mango","orange",4,6,True,"sai"]
d = ["car","bat"]
c.extend(d)
print(c)

# remove - removes the item it sees first
e = ["mango","orange",4,6,True,"sai"]
e.remove("mango")
print(e)

# pop - certain index we can reemove item
f= ["mango","orange",4,6,True,"sai"]
f.pop(3)
print(f)

#index() - used to get the index of specific item
g= ["mango","orange",4,6,True,"sai"]
k =g.index("sai")
print(k)

# count() - counts the item it repeted
h = ["mango","orange",4,6,True,"sai",4,4]
y =h.count(4)
print(y)

# sort()
i = [4,1,6,3,7]
i.sort()
print(i)

# reverse
j = ["mango","orange",4,6,True,"sai"]
j.reverse()
print(j)

#copy
a = ["mango","orange",4,6,True,"sai"]
copylist = a.copy()

print(copylist)

#clear()
z= ["mango","orange",4,6,True,"sai"]
z.clear
print(z)