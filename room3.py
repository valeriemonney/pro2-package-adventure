# room3.py - Definition des dritten Raums
class Room3:
    def __init__(self):
        self.name = "Raum 3"
        self.description = "Ein Waldweg mit einem alten Motorrad."
        self.items = ["Motorrad"]
        self.connections = {"links": "room2", "rechts": "room4"}  # Verbindungen zu Raum 2 und 4