# SNAKE-WATER-GUN GAME
'''
    SNAKE: 1
    WATER: -1
    GUN: 0
'''

import random

computer = random.choice([-1,0,1])
print("Input by the computer: ", computer)
youStr = input("Enter your choice: ")
youDict = { "S" : 1, "W" : -1, "G" : 0}
youDictReverse = { 1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youStr]
print("Input by you: ", you)

if computer == you:
    print("Match Drawn")

else:
    if (computer == -1 and you == 1):
        print("You Win!")
    elif (computer == -1 and you == 0):
        print("You Loose!")
    elif (computer == 1 and you == -1):
        print("You Loose!")
    elif (computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Loose!")

    else:
        print("Something went wrong")