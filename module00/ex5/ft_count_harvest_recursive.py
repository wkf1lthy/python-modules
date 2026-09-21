def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    count(1, n)

def count(day, n):
    if day == n:
        print("Day", n, "Harvest time!")
    else:
        print("Day", day)
        count(day + 1, n)
