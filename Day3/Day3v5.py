#Pizza Order

# Based on a user's order, work out their final bill.
# Small Pizza: $5
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for small pizza: +$2
# Pepperoni for medium or large pizza: +$3
# Extra cheese for any size pizza: +1

bill = 0
size = input("What size of pizza do you want? S, M, or L: ")
pepp = input("Do you want to add pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill = 15
    if pepp == "Y":
        bill+=2
        if cheese=="Y":
            bill+=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if cheese =="Y":
            bill +=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
elif size=="M":
    bill = 20
    if pepp == "Y":
        bill+=3
        if cheese=="Y":
            bill+=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if cheese =="Y":
            bill +=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
else:
    bill = 25
    if pepp == "Y":
        bill+=3
        if cheese=="Y":
            bill+=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if cheese =="Y":
            bill +=1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")

