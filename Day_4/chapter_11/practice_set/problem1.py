try:
    with open("chapter_11/1.txt","r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("chapter_11/practice_set/2.txt","r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("chapter_11/3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)