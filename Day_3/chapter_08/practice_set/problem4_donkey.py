word = "Donkey"

with open("chapter_08/practice_set/donkey_file.txt" , "r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("chapter_08/practice_set/donkey_file.txt" , "w") as f:
    f.write(contentNew)