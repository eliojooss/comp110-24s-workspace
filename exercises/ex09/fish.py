"""File to define Fish class."""


class Fish:
    """Fish Class."""
    age: int
    
    def __init__(self):
        """Create."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day."""
        self.age += 1
        return None