
from art import logo

def game_start():
    print(logo)
    print("Welcome to the secret auction program.")
    return ask_bidder()

def ask_bidder():
    bidder = input("What is your name?: ")
    if bidder in bidder_dictionaries["name"]:
        print("Name already taken.")
        return ask_bidder()
    bid = input("What's your bid?: €")
    while not bid.isdigit():
        bid = input("What's your bid?: €")
    bid = int(bid)
    if bid in bidder_dictionaries["bid"]:
        print("Bid already taken.")
        return ask_bidder()
    bidder_dictionaries["name"].append(bidder)
    bidder_dictionaries["bid"].append(bid)
    return next_bidder()

def next_bidder():
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidder == "yes":
        print("\n"*100)
        return ask_bidder()
    elif other_bidder == "no":
        print("\n" * 100)
        return result()
    else:
        print("Please try again.")
        return next_bidder()

def result():
    highest_bid = 0
    for bids in bidder_dictionaries["bid"]:
        if bids > highest_bid:
            highest_bid = bids
    highest_bid_index = bidder_dictionaries["bid"].index(highest_bid)
    print(f"Winner is {bidder_dictionaries["name"][highest_bid_index]}.")

bidder_dictionaries = {
    "name": [],
    "bid": [],
}

game_start()

