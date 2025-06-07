import random

def rollDice(noOfDice):
    if (noOfDice == '1'):
        random1 = random.randint(1,6)
        print(f" ({random1})")
    elif (noOfDice == '2'):
        random1 = random.randint(1,6)
        random2 = random.randint(1,6)
        print(f"({random1}, {random2})")
    else:
        print(f"can't roll more than two dice")


while (True):
    choice = input("do you want to roll the dice (Y/N): ").lower()

    if (choice == 'y'):
        diceNo = input("no. of dice you want to roll (1/2): ")
        rollDice(diceNo)
    elif(choice == 'n'):
        print("thanks! come back soon")
        break
    else:
        print("invalid option")
    






