class Room1:
    def __init__(self):
        self.name = "Raum 1"
        self.description = "Sie befinden sich in einem kleinen Raum. Hier liegt ein Kaugummi."
        self.items = ["Kaugummi"]
        self.connections = {"rechts": "room2"}  # Verbindung zu Raum 2
