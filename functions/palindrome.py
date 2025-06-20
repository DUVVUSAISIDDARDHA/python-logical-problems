
def palindrome(a):
    b = a[:: -1]
    if a ==b:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome("121")        
