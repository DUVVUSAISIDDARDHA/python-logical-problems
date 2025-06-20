try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a + b
    print(c)
except Exception as e:
    print("unknown exeption",e) 
    print("⚠️ This was a:", type(e).__name__)  