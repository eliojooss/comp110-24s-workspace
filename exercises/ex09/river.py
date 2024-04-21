"""File to define River class."""


__author__ = "730484781"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.fish = new_fish
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Remove fish."""
        for i in range(amount):
            self.fish.pop(i)
        return None

    def bears_eating(self):
        """Bears eating."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Check hunger."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Add fish."""
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Add bears."""
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        
    def one_river_week(self):
        """Simulate one week."""
        for i in range(7):
            self.one_river_day()
