#Randomization
#First import random module
import random
random_integer = random.randint(1,20) #inclusive and returns a whole number
print(random_integer)
random_decimal = random.random() #includes 1 but not 20
print(random_decimal)
random_decimal_5 = random.random() * 5 #gives floating point number less than 5
print(random_decimal_5)
