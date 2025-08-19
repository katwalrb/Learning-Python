#Nested elseif 
#Advanced BMI calculator
height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height**2,2)
print(f"Your BMI is {BMI:.2f}.")
if BMI <18.5:
    print("Your are underweight.")
elif BMI<25:
    print("You have a normal weight.")
elif BMI <=30:
    print("Your are overweight.")
elif BMI <=35:
    print("You are obese.")
else:
    print("You are clinically obese.")
