from caesar_cipher_art import caesar
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(encode_message_user, encode_shift_user, user_input):
    encoded_message = []
    num_shift(encode_shift_user)
    int_encode_shift_user = int(encode_shift_user)
    output = encrypt_decrypt(encode_message_user, int_encode_shift_user, encoded_message, user_input)
    print(f"Here's the {user_input}d result: \033[92m{output}\033[0m")
    restart()

def restart():
    restart_game = input("Type 'yes' if your want to go again. Otherwise type 'no'")
    restart_game.lower()
    if restart_game == "yes":
        player_start()
    elif restart_game == "no":
        print("Goodbye!")
    else:
        print("Wrong input, please try again.")
        restart()

def num_shift(encode_shift_user):
    if not encode_shift_user.isdigit():
        while not encode_shift_user.isdigit():
            print("Please insert a number!")
            encode_shift_user = input("Type the shift number:\n")

def encrypt_decrypt(encode_message_user, int_encode_shift_user, encoded_message, user_input):
    for char in encode_message_user:
        if char in letters:
            old_letter_index = letters.index(char)
            if user_input == "decode":
                new_letter_index = (old_letter_index - int_encode_shift_user) % 25
            else:
                new_letter_index = (old_letter_index + int_encode_shift_user) % 25
            encoded_message.append(letters[new_letter_index])
        else:
            encoded_message.append(char)
    output = "".join(encoded_message)
    return output

def player_start():
    print(caesar)
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_input.lower()
    while (user_input != "encode") and (user_input != "decode"):
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        user_input.lower()

    if user_input == "encode" or user_input == "decode":
        encode_message_user = input("Type your Message:\n").lower()
        encode_shift_user = input("Type the shift number:\n")
        encode(encode_message_user, encode_shift_user, user_input)

    else:
        print("Wrong input, please try again.")

player_start()
