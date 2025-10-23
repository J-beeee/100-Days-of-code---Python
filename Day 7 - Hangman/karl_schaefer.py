import random
from typing import List, Set

WORD_LIST: List[str] = ['python', 'programming', 'hangman', 'computer', 'game']
MAX_TRIES: int = 10

def choose_word(words: List[str]) -> str:
    # Return a random word from list
    return random.choice(words)

def display_word(word: str, guessed: Set[str]) -> str:
    # Show current word progress with underscores
    return ' '.join(letter if letter in guessed else '_' for letter in word)

def valid_guess(guess: str, guessed: Set[str]) -> bool:
    # Check guess for validity and repetition
    if not guess.isalpha() or not guess:
        print("Please enter a letter or the full word.")
        return False
    if guess in guessed:
        print("Already guessed.")
        return False
    return True

def get_guess(guessed: Set[str]) -> str:
    # Read and validate user guess
    while True:
        guess: str = input("Letter or full word: ").lower().strip()
        if valid_guess(guess, guessed):
            return guess

def play_hangman(word_list: List[str]) -> bool:
    # Run one round of hangman, returns win status
    word: str = choose_word(word_list)
    guessed: Set[str] = set()
    tries: int = MAX_TRIES

    print(f"Welcome to Hangman!\nThe word has {len(word)} letters.")

    while tries > 0:
        print(display_word(word, guessed))
        guess: str = get_guess(guessed)
        if len(guess) > 1:  # Word guess
            if guess == word:
                print(f"You won! The word was '{word}'.")
                return True
            print("Incorrect word.")
            tries -= 1
        elif guess in word:  # Correct letter
            guessed.add(guess)
            print("Correct!")
        else:  # Incorrect letter
            guessed.add(guess)
            print("Incorrect guess.")
            tries -= 1

        if all(letter in guessed for letter in word):
            print(f"Congratulations! The word was '{word}'.")
            return True

        print(f"Tries left: {tries}")

    print(f"Game over! The word was '{word}'.")
    return False

def main() -> None:
    # Loop for multiple games
    while True:
        play_hangman(WORD_LIST)
        again: str = input("Play again? (y/n): ").lower()
        if again.startswith('n'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()