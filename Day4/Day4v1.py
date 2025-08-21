#Write a virtual coin toss program.
#Generate a random number, either 0 or 1.
#Use that number to print out Heat or Tails

import random
a=random.randint(0,1)
if a == 0:
    print("Heads")
else:
    print("Tails")

