class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old")

class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        print(f"{self.name}:(Flower) {self.height}cm {self.age} days old {self.color}")
    
    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    
class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        print(f"{self.name}:(Tree) {self.height}cm {self.age} days old {self.trunk_diameter}")

    def produce_shade(self) -> None:
        shade_area = self.height // 5
        print(f"{self.name} provides {shade_area} square meters of shade")

class Vegetable(Plant):

    def __init__ (self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def get_info(self) -> None:
        print(f"{self.name}:(Vegetable) {self.height}cm {self.age} days old {self.harvest_season}")
    
    def nutritionnal(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden plant types ===")
    flower = Flower("Rose", 25, 30, "red color")
    flower.get_info()
    flower.bloom()
    flower1 = Flower("Sunflower", 56, 30, "yellow color")
    flower1.get_info()
    flower1.bloom()
    print("===========")
    tree = Tree("Oak", 500, 1825, 50)
    tree.get_info()
    tree.produce_shade()
    tree1 = Tree("Fir tree", 800, 1910, 48)
    tree1.get_info()
    tree.produce_shade()
    print("===========")
    vegetable = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    vegetable.get_info()
    vegetable.nutritionnal()
    vegetable1 = Vegetable("Carot", 35, 20, "summer harvest", "vitamin B")
    vegetable1.get_info()
    vegetable1.nutritionnal()
    print("===========")