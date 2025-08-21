#Rock Paper Scissors Game

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

options = [rock,paper,scissors]
ask = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if ask<0 or ask>2:
    print("Invalid choice. Try Again!")
else:
    user_shoot = options[ask]
    print(f"your choice: \n {user_shoot}")
    computer_shoot = random.choice(options)
    print(f"computer's choice: \n {computer_shoot}")

    if user_shoot == rock:
        if computer_shoot == paper:
            print("Computer Wins!")
        elif computer_shoot == scissors:
            print("You win!")
        else:
            print("Draw!")
    elif user_shoot == paper:
        if computer_shoot == scissors:
            print("Computer Wins!")
        elif computer_shoot == rock:
            print("You win!")
        else:
            print("Draw!")
    else:
        if computer_shoot == rock:
            print("Computer Wins!")
        elif computer_shoot == paper:
            print("You win!")
        else:
            print("Draw!")
    