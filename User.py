class User:
    all_posts = []

    def __init__(self, name, email, dl, user_post = None):
        self.name = name
        self.email = email 
        self.dl = dl 
        self.user_post = user_post

    def __str__(self):
        return f"My Name is {self.name}"
    
    def make_post(self):
        self.user_post = input(f"{self.name}, Please enter your post: ")
        self.all_posts.append(self.user_post)

user_alice = User("Alice", "Alice@mail.com", 12345)
user_bob = User("Bob", "Bob@mail.com", 54321)


user_alice.make_post()
user_bob.make_post()

print(User.all_posts)
