#Data Types

#String
"Hello"
print("Hello"[0])  #Subscripting
print("Hello"[-1])
print("123"+"456")

#Integer
print(123+456)

#Float
print(123.5+456.7)
print(3.14)

#Boolean
True 
False

#Type
num_char = len(input("What is you name? "))
print(type(num_char))

#Type Casting
new_num_char = str(num_char)
print("Your name has "+ new_num_char + " characters")
print(100+float("23.4"))
print(str(100)+str(23.4))

two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0])+int(two_digit_number[1]))

#BMI Calculator (in 2 decimal places)
height = input("Height in m: ")
weight = input("Height in kg: ")
bmi = round(float(weight)/float(height)**2,2)
print("BMI = "+ str(bmi))

print(8//3) #floor division
a = 4/2
a/=2
print(a)

#f-string
weight = 55
height = 1.5
isOkay = True
print(f"Your weight is {weight}, your height is {height}, and your BMI is Okay is {isOkay}")

#Remaining Life Calculator Considering 90 Years as the Limit
age = input("What is your current age?")
years_remain = 90 - int(age)
months_remain = years_remain*12
weeks_remain = years_remain*52
days_remain = years_remain*365
print(f"You have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left")

#Tip calculator
total = float(input("What is the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = float(input("How many people to split the bill? "))
each_tip = round((total + tip/100*total)/people,2)
print(f"Each person should pay: ${each_tip:.2f}")



