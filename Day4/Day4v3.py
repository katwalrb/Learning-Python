#Write a program to select a random name from a list. 
import random
names_string =input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ") #splits the string into list

index = random.randint(0,len(names)-1) #indexing is from zero but len() gives total i.e. 1,2,3...
print(f"{names[index]} will pay the bill.")

#another way of doing it
print(f"{random.choice(names)} will pay the bill.")