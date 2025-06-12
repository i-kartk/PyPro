import random 

player = input("enter your choice (r for rock , p for paper , s for scissor)").lower()
computer = random.choice(['r','s','p'])


choices = {'r':'🪨', 'p':'📜','s':'✂️'}

if (player == computer):
    print(f"its a tie \n you choose : {choices[player]} \n computer choice : {choices[computer]}")

elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
    print(f"You WIN!! \n you choose : {choices[player]} \n computer choice : {choices[computer]}")
else :
    print(f"You LOSE !! \n you choose : {choices[player]} \n computer choice : {choices[computer]}")
