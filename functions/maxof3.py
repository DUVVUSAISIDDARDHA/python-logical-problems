
def maxnum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
         return b
    else:
        return c
num1 = input("enter a number 1")
num2 = input("enter a number 2")
num3 = input("enter a number 3")

max =maxnum(num1,num2,num3)
print(max)

    
