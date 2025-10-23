import random
import art

def game_initialization():
    print("\n"*20)
    print(art.logo)
    r_number = random.randint(1, 100)
    mode = input("Welcome to the Number Guessing Game!\nI'm thinking og a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard',\n")
    already_guessed = []
    difficulty(r_number, mode, already_guessed)

def difficulty(r_number, mode, already_guessed):
    if mode == "easy":
        lives = 10
        return guess(lives, r_number, already_guessed)
    elif mode == "hard":
        lives = 5
        return guess(lives, r_number, already_guessed)
    else:
        return "wrong input, please try again", game_initialization()

def guess(lives, r_number, already_guessed):
    while lives > 0:
        u_guess = input("Make a guess:")
        if u_guess.lstrip('-').isdigit():
            u_guess= int(u_guess)
            if u_guess > 100:
                return print("That makes no sense."), guess(lives, r_number, already_guessed)
            elif u_guess < 0:
                return print("That makes no sense."), guess(lives, r_number, already_guessed)
            lives -= 1
            return compare(lives, r_number, u_guess, already_guessed=already_guessed)
        else:
            return guess(lives, r_number, already_guessed)
    else:
        return compare(lives, r_number, u_guess="", already_guessed=already_guessed)

def compare(lives, r_number, u_guess, already_guessed):
    if u_guess in already_guessed:
        lives +=1
        return print("You already picked that number."), guess(lives, r_number, already_guessed)
    else:
        already_guessed.append(u_guess)
    if u_guess == r_number:
        print(f"You picked the right Number: {r_number} You won!")
        return restart()
    elif lives == 0:
        print(f"You lost - Lives: {lives} - Number: {r_number}")
        return restart()
    elif u_guess > r_number:
        print(f"Too high! - Lives: {lives}")
        return guess(lives, r_number, already_guessed)
    elif u_guess < r_number:
        print(f"Too low! - Lives: {lives}")
        return guess(lives, r_number, already_guessed)
    return None

def restart():
    u_restart = input("You wanna restart? 'y' or 'n': ")
    if u_restart == "y":
        return game_initialization()
    else:
        return print("Have a nice day.")

game_initialization()
