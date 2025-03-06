from room1 import Room1
from room2 import Room2
from room3 import Room3
from room4 import Room4

def create_rooms():
    r1 = Room1()
    r2 = Room2()
    r3 = Room3()
    r4 = Room4()

    # Verbindungen setzen (sollten mit den `connections` übereinstimmen)
    rooms = {
        "room1": r1,
        "room2": r2,
        "room3": r3,
        "room4": r4
    }
    return rooms
