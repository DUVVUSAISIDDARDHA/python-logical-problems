N = int(input("enter a number from 0 to 31"))
if N<0 and N > 31:
    print("enter correct number ")
else:
    print("2^n table is:") 
for i in range(N+1):
    power = 2 ** i
    print("2^"+ str(i)+ "=" + str(power))
