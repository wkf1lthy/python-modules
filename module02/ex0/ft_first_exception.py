def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        return f"'{temp_str}' is not a valid number"
    if temp > 40:
        return f"{temp}°C is too hot for plants (max 40°C)"
    if temp < 0:
        return f"{temp}°C is too cold for plants (min 0°C)"
    return temp

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        print(f"Testing temperature: {t}")
        result = check_temperature(t)
        if isinstance(result, int):
            print(f"Temperature {result}°C is perfect for plants!")
        else:
            print(f"Error: {result}")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()