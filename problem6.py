n = int(input("Enter a number: "))

if n <= 1:
    print("Enter a number greater than 1.")
else:
    print("The prime factors are:")

    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
        else:
            i += 1

    
    if n > 1:
        print(n)
