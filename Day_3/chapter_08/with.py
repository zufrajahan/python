f = open("file.txt")
print(f.read())
f.close()

# this above can be done using with statement
with open("file.txt") as f:
    print(f.read()) # here you dont need to explicitly close