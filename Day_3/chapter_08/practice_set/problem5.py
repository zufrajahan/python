words = ["Donkey","bad","ganda"]

with open("chapter_08/practice_set/donkey_file.txt" , "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("chapter_08/practice_set/donkey_file.txt" , "w") as f:
    f.write(content)