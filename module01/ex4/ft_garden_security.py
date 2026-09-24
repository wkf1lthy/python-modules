class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, height: int) -> None:
        if height > 0:
            self.height = height
            print(f"Height updated: {height} [OK]")
        else:
            print(f"Invalid operation attempted {height}cm [REJECTED]")
            print(f"Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self.age = age
            print(f"Age updated: {age} [OK]")
        else:
            print(f"Invalud operation attempted {age} [REJECTED]")
            print(f"Security: Negative age rejected")
    
    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> None:
        print(f"Current plant: {self.name} {self.height}cm {self.age} days old")

if __name__ == "__main__":
    print("=== Garden security system ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(50)
    plant.set_height(-1)
    plant.set_age(-8000)
    plant.get_info()