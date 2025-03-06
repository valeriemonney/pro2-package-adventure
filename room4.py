# room4.py - Definition des vierten Raums
class Room4:
    def __init__(self):
        self.name = "Raum 4"
        self.description = "Hier steht ein Kanister mit Benzin."
        self.items = ["Benzin"]
        self.connections = {"links": "room3"}  # Verbindung zu Raum 3
