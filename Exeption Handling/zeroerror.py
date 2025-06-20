
try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("dont give 0 as input")   