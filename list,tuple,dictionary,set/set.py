# add() - adds at end
a = {1,3,5,"sai"}
a.add("obito")
print(a)

# remove() - removes elemnet u want if element notfound error occurs
b = { 1,2,4,"vivek"}
b.remove("vivek")
print(b)

# discard() - removes an element we want and no error if element is not present
c = {1,3,5,7}
c.discard("sai")
print(c)

# pop() - removes random item
d = {1,2,3,4,5}
d.pop()
print(d)

# clear
exec = {1,3,5,"sai"}
exec.clear()
print(exec)

# copy()
e = {1,3,5,"sai"}
f =e.copy()
print(f)

# difference()
x = {1,2,3,4}
y = {2,3,4,5}
z=x.difference(y)
print(z)

# union()
p = {1,2,3,4}
q = {2,3,4,5}
r=p.union(q)
print(r)

# intersection()

xx = {1,2,3,4}
yy = {2,3,4,5}
zz=xx.intersection(yy)
print(zz)

#update()
a = {1,3,5,"sai"}
a.update(["vivek"])
print(a)



