class Plant:
    """A class for plants representing their name, age in days, height in cm"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age #ajout de self pour que la plant s'affiche seule et qu'on puisse en afficher plusieurs

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old") #fonction qui va afficher les infos des plantes sans qu'on ait a devoir a print 3x d'affile

if __name__ == "__main__":
    print("== Garden plant data ==")
    plant1 = Plant("Cosmos", 2, 15)
    plant1.get_info()
    plant2 = Plant("Sunflower", 20, 25)
    plant2.get_info()
    plant3 = Plant("Rose", 25, 30)
    plant3.get_info()



