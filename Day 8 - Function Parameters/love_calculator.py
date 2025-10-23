


def calculate_love_score(girl, boy):
    combined = girl + boy
    combined.lower()
    true_counter = sum(combined.count(char) for char in "true")
    love_counter = sum(combined.count(char) for char in "love")

    love_counter = f"{true_counter}{love_counter}"
    print(f"{love_counter}")


calculate_love_score("stinker", "Sammy")