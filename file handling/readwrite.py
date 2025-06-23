
file = open(r"C:\Users\saisi\OneDrive\Documents\demo.txt","r+")
content = file.read()
file.seek(0)
print(content)
file.write("o")
file.close()