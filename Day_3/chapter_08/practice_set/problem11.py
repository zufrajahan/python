with open("chapter_08/practice_set/old.txt") as f:
    content=f.read()

with open("rnamed_by_python.txt","w") as f:
    f.write(content)