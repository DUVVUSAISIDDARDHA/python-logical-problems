user_name = input("what is your name(min 3 char)?")
if len(user_name)>=3:
    message = "Hi <<user name>>, how are you?"
    final_msg= message.replace("<<user name>>",user_name)
    print(final_msg)        
else:
    print("name must have atleast 3 char")

