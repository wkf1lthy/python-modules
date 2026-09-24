class Plant:
    total_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1
    
    def ageplus(self, amount: int) -> None:
        self.age += amount

    def cmplus(self, amount: int) -> None: 
        self.height += amount 
    
    def get_info(self) -> None:
            print(f"{self.name}: {self.height}cm {self.age} days old")

if __name__ == "__main__":
    print("=== Plant factory output ===")
    plant1 = Plant("Cactus", 18, 180)
    plant1.ageplus(3)
    plant1.cmplus(1)
    plant1.get_info()
    plant2 = Plant("Sunflower", 35, 25)
    plant2.ageplus(3)
    plant2.cmplus(40)
    plant2.get_info()
    plant3 = Plant("Rose", 2, 2)
    plant3.ageplus(10)
    plant3.cmplus(10)
    plant3.get_info()
    plant4 = Plant("Cosmos", 15, 18)
    plant4.ageplus(1)
    plant4.cmplus(1)
    plant4.get_info()
    plant5 = Plant("Fern", 15, 120)
    plant5.ageplus(3)
    plant5.cmplus(2)
    plant5.get_info()
    print(f"=== Total plants created: {Plant.total_plants} ===")