try:
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    c ="hi"
    op = input("enter a operator: + ,- ,/ ,%")
    if op == "+":
       print("sum is :", a +b+c)
    elif op == "-":
       print("sub is:",a - b)
    elif op == "*":
       print("mult is :",a*b)
    elif op == "/":
       print("mult is :",a/b)
    else:
       print("enter operator")
except ZeroDivisionError:
   print("dont enter 0")
except TypeError:
   print("type error")
except ValueError:
   print("value error")
                
