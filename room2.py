# room2.py - Definition des zweiten Raums
class Room2:
    def __init__(self):
        self.name = "Raum 2"
        self.description = "Hier starten Sie Ihr Abenteuer."
        self.items = []
        self.connections = {"links": "room1", "rechts": "room3"}  # Verbindungen zu Raum 1 und 3
