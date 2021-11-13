from art import logo
import os
from time import sleep

print(logo)

def clear_screen():
    # for macos and linux
    if os.name == 'posix':
        _ = os.system('clear')
    # for windows
    else:
        _ = os.system('cls')



bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with highest bid of ${highest_bid}.") 

while not bidding_finished:
    name = input("what is your name ?\n")
    price = int(input("what's your bidding?\n$"))
    bids[name] = price
    should_continue = input("Are there any other users? Type 'yes' or 'no'\n").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear_screen()
