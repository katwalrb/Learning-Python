#Ticketing incorporating midlife crisis
height = int(input("What is your height? "))
bill=0
if height>=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age<12:
        bill = 5
    elif age<=18:
        bill = 7
    elif age>=45 and age<=55:
        print("Everything is going to be Okay. Have a free ride on us.")
    else:
        bill = 10
    photo = input("Do you want your photo taken? Y or N: ")
    if photo == "Y":
        bill+=3
        print(f"Your total is ${bill}.")
    else:
        print(f"Your total is ${bill}.")
else:
    print("You cannot ride the rollercoaster!")
