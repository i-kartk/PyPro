import random

def takeInput():
    while True: 
        try:
            num1 = int(input("enter the starting number:" ))
            num2 = int(input("enter the ending number: "))
            
            if (num1 >= num2):
                print("the starting number must be smaller than the ending number")
                continue
            return num1,num2

        except ValueError:
            print("enter the valid integer values")

a,b = takeInput()

ranNum = random.randint(a,b)
tries = 0
attempts = 7

print("You have 7 attempts to guess the right answer '''GOOD LUCK'''")

while(tries < attempts):
    try:
        num = int(input(f"enter the number (guess between {a} to {b}): "))

        if num < a or num > b:
            print(f"Please guess a number within the range {a} to {b}.")
            continue

        tries += 1    # this is to avoid the invalid step from counting that's why its here.
        if(ranNum > num):
            print(f"Too low , try again")
        elif(ranNum < num):
            print(f"Too high , try again")
        else:
            print(f"CONGRATULATIONS !!,  you guess the right number {tries} tries ")
            break
    except ValueError:
        print("enter a valid integer value")
if (tries == attempts) :
    print(f"You have used all the {attempts} attempts. The number you have to guess is {ranNum}.")
        
