class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    
    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old")

    def ageplus(self, amount: int) -> None:
        self.age += amount

    def cmplus(self, amount: int) -> None: 
        self.height += amount 
if __name__ == "__main__":

    print("=== Day1 ===")
    plant = Plant("Rose", 25, 30)
    starting_height = plant.height
    plant.get_info()
    for i in range(1, 8):
        plant.ageplus(1)
        plant.cmplus(1)
    print("=== Day7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.height - starting_height}cm")