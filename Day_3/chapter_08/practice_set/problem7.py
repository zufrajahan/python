

with open("chapter_08/practice_set/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present . line no {lineno}")
        break
    lineno += 1

else:
        print("no python ")