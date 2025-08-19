#Logical operators
#Take two peopl's names and check for the number of
#times the letters in the word TRUE occurs and the
#number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.
#Lovescore<10 or >90, coke and mentos
#Lovescore>40 and <50, alright together
#Otherwise, just the score

print("Welcome to the Love Calculator!")
name1 = input("Man's name: ")
name2 = input("Woman's name: ")

low_name1 = name1.lower()
low_name2 = name2.lower()
sum1 = (low_name1.count("t") + low_name1.count("r") +low_name1.count("u")+low_name1.count("e")+
        low_name2.count("t") + low_name2.count("r") +low_name2.count("u")+low_name2.count("e"))
sum2 = (low_name1.count("l") + low_name1.count("o") +low_name1.count("v")+low_name1.count("e")+
        low_name2.count("l") + low_name2.count("o") +low_name2.count("v")+low_name2.count("e"))
score = int(str(sum1)+str(sum2))

if score<10 or score>90:
    print(f"Your score is {score}. You go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}. You go alright together.")
else:
    print(f"Your score is {score}.")



