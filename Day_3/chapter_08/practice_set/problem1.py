f = open("chapter_08/practice_set/poem.txt")
content = f.read()
if("Twinkle" in content):
    print("present hai yar")
else:
    print("nahi hai bhai")
f.close()