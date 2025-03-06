from rooms import create_rooms
from player import Player
from commands import process_command

def main():
    rooms = create_rooms()
    player = Player("room2")  # Start in Raum 2
    print("Willkommen zum Textadventure!")
    print(rooms[player.current_room].description)

    while True:
        command = input("> ").lower()
        if command in ["exit", "quit"]:
            print("Spiel beendet.")
            break
        result = process_command(player, command, rooms)
        print(result)

if __name__ == "__main__":
    main()
