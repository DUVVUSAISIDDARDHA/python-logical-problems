N = int(input("enter a number:"))
if N <=0:
    print("enter a number not 0")
else:
    harmonic = 0.0
    print("harmonic series is:")
for i in range(1,N+1):
    harmonic = harmonic + 1/i
print(harmonic)           