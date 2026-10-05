def water_plants(plant_list: list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    good_list = ["tomato", "lettuce", "carrots"]
    bad_list = ["tomato"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(bad_list)
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
    