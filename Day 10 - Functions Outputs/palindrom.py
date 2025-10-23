user_input = input("Write your palindrome.\n")

def palindrom(x):
    return x[::-1]

user_text = palindrom(user_input)
if user_text == user_input:
    print(f"Your text is a palindrom: {user_text} == {user_input}")
else:
    print(f"Your text is no palindrom: {user_text} == {user_input}")
