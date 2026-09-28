class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def get_description(self) -> str:
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant): 
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_description(self) -> str:
        return f"{super().get_description()}, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_description(self) -> str:
        return f"{super().get_description()}, Prize points: {self.prize_points}"

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
    @classmethod
    def create_garden_network(cls):
        return[cls("Alice"), cls("Bob")]
    def report(self) -> None: 
        total_growth = 0
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_description()}")
            total_growth += plant.height - plant.initial_height
        print(f"Plants added: {len(self.plants)}, Total growth: {total_growth}cm")



if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice, bob = GardenManager.create_garden_network()
    alice.add_plant(Plant("Oak Tree", 101))
    alice.add_plant(FloweringPlant("Rose", 26, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 51, "yellow", 10))
    alice.grow_all()
    alice.report()
    
     