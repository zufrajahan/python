letter = ''' Dear <|name|>,
            You are selected!   
            <|date|>'''

print(letter.replace("<|name|>","zufra").replace("<|date|>","12-12-2021"))