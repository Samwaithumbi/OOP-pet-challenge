class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 9  # Default mid-level values
        self.energy = 4
        self.happiness = 7
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        self.energy = min(self.energy + 5, 10)

    def play(self):
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

    def get_status(self):
        print(f"--- {self.name}'s  Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("------------------------")

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"{self.name} knows the following tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print("No tricks learned yet.")
