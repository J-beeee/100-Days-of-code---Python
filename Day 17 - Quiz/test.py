#PascalCase = DiesIstEineNachricht -> ClassName
#camelCase = diesIstEineNachricht
#snake_case = dies_ist_eine_nachricht -> everything_else

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

        print("new User being created...")
    pass

user_1 = User("001", "julia")
user_2 = User("002", "ivy")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)