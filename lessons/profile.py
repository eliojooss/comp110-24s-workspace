"""Practice writing a class."""

class Profile:
    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create a new profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str):
        """If profile is public, print msg."""
        if self.private == False:
            print(msg)

user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool")