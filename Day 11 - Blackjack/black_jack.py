import random
import art

cards = [11, 2, 3, 4, 5, 6,7 , 8, 9, 10, 10, 10, 10]

def game_start():
    print(art.logo)
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while start == "y":
       return distribute_cards()
    else:
        return print("Have a nice Day, see u soon.")

def distribute_cards():
    player_cards = {
        "user_cards": [],
        "computer_cards": [],
    }

    for _ in range(2):
        player_cards["user_cards"].append(random.choice(cards))
        player_cards["computer_cards"].append(random.choice(cards))
    sum_user_cards = sum(player_cards["user_cards"])
    sum_computer_cards = sum(player_cards["computer_cards"])
    print(f"Your cards: {player_cards["user_cards"]}, current score: {sum_user_cards}")
    print(f"Computer's first card: {player_cards["computer_cards"][0]}")
    if sum_user_cards > 21:
        player_cards["user_cards"][0] = 1
        print("Your 11 count as 1 now.")
        print(player_cards["user_cards"])
        sum_user_cards = sum(player_cards["user_cards"])
        more_cards(player_cards, sum_user_cards)
    elif sum_computer_cards > 21:
        player_cards["computer_cards"][0] = 1
        print("Computer Card 11 count as 1 now.")
    elif sum_user_cards >= 21:
        result(player_cards, sum_user_cards)
    else:
        more_cards(player_cards, sum_user_cards)

def more_cards(player_cards,sum_user_cards):
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y" and sum_user_cards < 21:
        player_cards["user_cards"].append(random.choice(cards))
        sum_user_cards = sum(player_cards["user_cards"])
        print(f"Your cards: {player_cards["user_cards"]}, current score: {sum_user_cards}")
        if sum_user_cards > 21 and (11 in player_cards["user_cards"]):
            eleven_index = player_cards["user_cards"].index(11)
            player_cards["user_cards"][eleven_index] = 1
            print("Your 11 count as 1 now.")
            sum_user_cards = sum(player_cards["user_cards"])
            if sum_user_cards == 21:
                result(player_cards, sum_user_cards)
            elif sum_user_cards > 21:
                result(player_cards, sum_user_cards)
            else:
                more_cards(player_cards, sum_user_cards)
        elif sum_user_cards < 21:
            more_cards(player_cards,sum_user_cards)
        else:
            result(player_cards, sum_user_cards)
    else:
        result(player_cards, sum_user_cards)
def result(player_cards, sum_user_cards):
    sum_computer_cards = sum(player_cards["computer_cards"])
    while sum_computer_cards < 17:
        player_cards["computer_cards"].append(random.choice(cards))
        sum_computer_cards = sum(player_cards["computer_cards"])
    while sum_computer_cards > 21 and (11 in player_cards["computer_cards"]):
        eleven_index = player_cards["computer_cards"].index(11)
        player_cards["computer_cards"][eleven_index] = 1
        return result(player_cards, sum_user_cards)
    sum_computer_cards = sum(player_cards["computer_cards"])
    if sum_user_cards < sum_computer_cards <=21:
        print("You lost!")
        print(f"Computer Cards: {player_cards["computer_cards"]}")
        print(f"Your Cards: {player_cards["user_cards"]}")
        print(f"Your score: {sum_user_cards}\nComputer score: {sum_computer_cards}")
        return game_start()
    elif sum_computer_cards > sum_user_cards <= 21 or sum_computer_cards < sum_user_cards == 21:
        print("You Won!")
        print(f"Computer Cards: {player_cards["computer_cards"]}")
        print(f"Your Cards: {player_cards["user_cards"]}")
        print(f"Your score: {sum_user_cards}\nComputer score: {sum_computer_cards}")
        return game_start()
    elif sum_user_cards == sum_computer_cards:
        print("Draw")
        print(f"Computer Cards: {player_cards["computer_cards"]}")
        print(f"Your Cards: {player_cards["user_cards"]}")
        print(f"Your score: {sum_user_cards}\nComputer score: {sum_computer_cards}")
        return game_start()
    else:
        print("You lost!")
        print(f"Computer Cards: {player_cards["computer_cards"]}")
        print(f"Your Cards: {player_cards["user_cards"]}")
        print(f"Your score: {sum_user_cards}\nComputer score: {sum_computer_cards}")
        return game_start()

game_start()
