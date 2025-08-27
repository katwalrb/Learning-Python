import random
from hangman_wordlist import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)
print(f"word is: {chosen_word}")
life = 7

word_list = []
for letter in chosen_word:
    word_list += letter

display = []
for _ in chosen_word:
    display += "-"
print(display)
while display != word_list and life != 0:
    count = 0     
    guess = input("Guess a letter in the word: ")
    if guess in display:
        print(f"You've already guessed {guess}.")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            count += 1
    print(display)
    if count == 0:
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life.")
        print(stages[life-1])
        life -= 1
    
    if display == word_list:
        print("You guessed it correctly. Congratulations!")
    elif life == 0:
        print("You lost! \nGame Over!!!")