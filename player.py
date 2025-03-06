class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        if direction in rooms[self.current_room].connections:
            self.current_room = rooms[self.current_room].connections[direction]
            return f"Du bist jetzt in {rooms[self.current_room].name}."
        else:
            return "Hier kannst du nicht lang."

    def take(self, item, rooms):
        if item in rooms[self.current_room].items:
            self.inventory.append(item)
            rooms[self.current_room].items.remove(item)
            return f"{item} aufgenommen."
        return "Das gibt es hier nicht."
s