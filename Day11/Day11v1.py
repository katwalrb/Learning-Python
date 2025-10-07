#BlackJack

from clear_function import clear
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    """Takes a list of cards and return the sum"""
    if sum(card_list)==21 and len(card_list)==2:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list[card_list.index(11)] = 1
    return sum(card_list)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw!"
    elif comp_score == 0:
        return "Computer wins! Computer has a Blackjack."
    elif user_score == 0:
        return "You win! You got a Blackjack."
    elif user_score > 21:
        return "You went over. You lose!"
    elif comp_score > 21:
        return "Computer went over. You win!"
    elif user_score > comp_score:
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    user_cards=[]
    computer_cards=[]
    game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' for another card or type 'n' to pass: ")
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    while comp_score!=0 and comp_score <17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)
    print(f"Computer final cards: {computer_cards}, total score = {comp_score}")        
    print(compare(user_score, comp_score))   
while input("Type 'y' to play BlackJack or type'n' to exit: ") == "y":
    clear()
    play_game()


