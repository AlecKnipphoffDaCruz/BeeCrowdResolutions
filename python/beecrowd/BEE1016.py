
"""
This program calculates the time (in minutes) it takes for car Y, traveling at 90 km/h, to gain a specified distance over car X, traveling at 60 km/h, when both cars start at the same time and move in the same direction.
The user provides the distance (in kilometers) as input. The program outputs the required time in minutes for car Y to be ahead of car X by the given distance, followed by the word "minutos".
Example:
Input: 30
Output: 60 minutos
Input: 110
Output: 220 minutos
"""
def main():
    carx = 60
    cary = 90
    distance = int(input())
    relative_speed = cary - carx
    time_minutes = (distance / relative_speed) * 60
    print(f"{time_minutes:.0f} minutos")