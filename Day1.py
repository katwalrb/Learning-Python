#Print function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("Hello World!\nHello World!\nHello World!")
print("Hello " + "World!") #string concatenation

#Debugging
#Fix the code below
#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
#  print('e.g. print("Hello " + "World!")')
#print(("New lines can be created with a backslash and n.")
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "World!")')
print("New lines can be created with a backslash and n.")

#Input function
input("What is your name? ")
print("Hello" + " " + input("What is your name? "))

#A program to print the number of characters in your name
name = input("What is your name? ")
length = len(name)
print(length)

print(len(input("What is your name? ")))

#Python variables
name = input('What is your name? ')
print(name)
name = "Rewat"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)

#Switch the vairables value
a = input("a: ")
b = input("b: ")
#code to switch the values
x = a
a = b
b =x
print("a = " + a)
print("b = " + b)

#Band name generator
print("Welcome to the Band Name Generator")
city = input("Name of the city you grew up in: \n")
pet = input ("Name of your pet: \n")
print("The name of your band is " + city + " " + pet)
