class User:

    def __init__(self, username=input('enter username: '), userfamily=input('enter userfamily: ')):
        self.username = username
        self.userfamily = userfamily
        print(f"{self.username} {self.userfamily}")


User()
