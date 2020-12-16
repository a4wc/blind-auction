from replit import clear
from art import logo

print(logo)

bid_dict = {}

def silent_auct():
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    
    bid_dict[name] = bid

    more = input("Are there any more bidders?").lower()
    if more == "yes":
        clear()
        silent_auct()
    elif more == "no":
        clear()

def find_highest_bidder(bidders):
    highest_bidder = ""
    highest_bid = 0
    for i in bidders:
        if bidders[i] > highest_bid:
            highest_bidder = i
            highest_bid = bidders[i]

    print(f"Highest bidder is {highest_bidder} with a bid of {highest_bid}")


silent_auct()
find_highest_bidder(bid_dict)

