
import random
while True:
    dice=random.randint(1,6)
    print(dice)
    if dice==6:
        prize=random.randint(1,6)
        print(prize)
    else:
        print("you lost")
        break            


 