#Blind Auction

from clear_function import clear
from auction_art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding_continues = True
auction_bids = {}
while bidding_continues:
    name = input("What is your name? ")
    bid = int(input("What is your bid amount? "))
    auction_bids[name] = bid
    bidders_remaining=input("Are there any more bidders? Type 'yes' or 'no'. ")
    if bidders_remaining=='no':
        bidding_continues =False
        clear()
    else:
        clear()

bid_value = 0
highest_bid = 0
for person in auction_bids:
    bid_value = auction_bids[person]
    if bid_value>=highest_bid:
        highest_bid = bid_value
winning_bid = highest_bid

for bidder in auction_bids:
    if winning_bid == auction_bids[bidder]:
        print(f"The winner is {bidder} with a bid of ${winning_bid}.")



