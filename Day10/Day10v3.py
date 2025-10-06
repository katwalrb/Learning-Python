#Calculator

from calculator_art import logo
print(logo)

def calculate():
    def add(n1,n2):
        return n1+n2
    def subtract(n1,n2):
        return n1-n2
    def multiply(n1,n2):
        return n1*n2
    def divide(n1,n2):
        return n1/n2

    operations = {
        '+': add, 
        '-' : subtract,
        '*' : multiply,
        '/' : divide,
    }

    num1 = float(input("What is the first number?: "))
    for i in operations:
        print(i)

    continue_calc = True
    while continue_calc:


        operation_symbol = input("Choose an operation: ")
        num2 = float(input("Enter the new number: "))
        caclulation = operations[operation_symbol]
        answer = round(caclulation(num1,num2),2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        should_continue = input("Type 'y' to continue,'r' to restart, or 'n' to quit: ")
        if should_continue == 'n':
            continue_calc = False
        elif should_continue == 'r':
            continue_calc = False
            calculate()

calculate()

