# Write File
data = "hello"
with open("test.txt","w") as fp:
    fp.write(data)

# read File
with open("test.txt","r") as fp:
    print("==== Result of reading the file")
    print(fp.read())