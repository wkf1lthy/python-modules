class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old")

class FloweringPlant(Plant): 
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        super().get_info()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        print(f"{self.name} (blooming)")

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self) -> None:
        super().get_info()
        print(f"Prize points: {self.prize_points}")
class GardenManager:
    total_gardens = 0
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1
    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")
    class GardenStats:
            @staticmethod
            def ave_height(plants: list) -> float:
                if len(plants) == 0:
                    return 0.0
                total = 0
                for plant in plants:
                    total = total + plant.height
                return total / len(plants)
    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow")
        for plant in self.plants:
            plant.height += 1
        print(f"{plant.name} grew 1cm")
        

if __name__ == "__main__":
    sunflower = PrizeFlower("Sunflower", 51, 45, "yellow", 10)
    sunflower.get_info()
     