class UserSystem:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name):
        self.users[user_id] = name

    def display_users(self):
        print(self.users)

    def update_user(self, user_id, new_name):
        if user_id in self.users:
            self.users[user_id] = new_name

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]


user = UserSystem()
user.create_user(1, "XYZ")
user.create_user(2, "ABC")
user.display_users()
user.update_user(1, "Updated XYZ")
user.delete_user(2)
user.display_users()