import random
n = int(input("how many times do u wanna flip"))
if n<=0:
    print("enter positive number")
else:
    heads =0
    tails= 0
for i in range(n):
   result = random.random() 
   if result < 0.5:
     tails = tails +1
   else :
      heads = heads +1
percentage_heads = (heads /n)*100
percentage_tails = (tails /n)*100

print(percentage_heads)
print(percentage_tails)