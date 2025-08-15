balance = 5000
print("Welcome")
while True:
    print("1. Balance Inquiry")
    print("2. Cash Deposit")
    print("3. Cash Withdrawl")
    print("4. Exit")
    ask =int(input("Enter the option number: "))
    if ask == 1:
        print(f"Your balance is {balance}")
    elif ask == 2:
        deposit = float(input("Enter the amount to deposit: "))
        if deposit>0:
            balance+=deposit
            print(f"Successfully deposited.\n Your new balance is {balance}.")
        else:
            print("Enter a valid number.")
    elif ask == 3:
        withd = float(input("Enter the amount to withdraw: "))
        if withd>0:
            balance-=withd
            print(f"Withdraw successfull. Please collect your cash.\n Your remaining balance is {balance}.")
        else: 
            print("Enter a valid number.")
    elif ask == 4:
        print("Thank you for choosing our services.")
        break
    else:
        print("Please try again")
        break
    break
