f= open("chapter_08/file.txt")
lines = f.readlines() # function that is used to read lines it gives a list
print(lines,type(lines))

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()