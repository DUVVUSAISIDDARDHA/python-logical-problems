year = int(input("enter year"))
if year<1000 and year >9999:
    print("enter 4 digit number")
else:
    if (year % 4 == 0 and year % 100 != 0)   or   (year % 400 ==0):
        print("leap year")
    else:
        print("Not a leap year")    

