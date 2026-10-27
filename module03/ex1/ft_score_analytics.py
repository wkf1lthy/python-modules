import sys

def score_analytics():
    print("=== Player Score Analytics ===")
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not numbers:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {numbers}")
    print(f"Total players: {len(numbers)}")
    print(f"Total score: {sum(numbers)}")
    print(f"Average score: {sum(numbers) / len(numbers)}")
    print(f"High score: {max(numbers)}")
    print(f"Low score: {min(numbers)}")
    print(f"Score range: {max(numbers) - min(numbers)}")


if __name__ == "__main__":
    score_analytics()