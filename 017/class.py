class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User(1, "josh")

print(user_1.id)
print(user_1.username)