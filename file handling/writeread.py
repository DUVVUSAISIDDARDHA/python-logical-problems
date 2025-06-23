file = open(r"C:\Users\saisi\OneDrive\Documents\demo.txt","w+")

file.write("hi bro")
file.seek(0)
content = file.read()
print(content)