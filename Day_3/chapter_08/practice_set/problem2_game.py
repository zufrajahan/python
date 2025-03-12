import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    # fetch the hiscore
    with open("chapter_08/practice_set/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0    
    print(f"Your score {score}")
    if(score > hiscore):
        # write the hiscore to file
        with open("chapter_08/practice_set/hiscore.txt","w") as f:
            f.write(str(score))
          
    return score

game()