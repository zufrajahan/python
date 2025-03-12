with open("chapter_08/practice_set/log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
else:
    print("no python ")