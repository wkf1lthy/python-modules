import math

def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            coords = raw.split(",")
            x = float(coords[0])
            y = float(coords[1])
            z = float(coords[2])
            break
        except (ValueError, IndexError):
            print("Invalid syntax")
    return(x, y, z)
    
if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    e1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(e1, 4)}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    e2 = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(e2, 4)}")
    
    