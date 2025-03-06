def process_command(player, command, rooms):
    parts = command.split()
    if len(parts) == 1:
        if parts[0] == "schaue":
            return rooms[player.current_room].description
    elif len(parts) == 2:
        action, target = parts
        if action == "nimm":
            return player.take(target, rooms)
    elif len(parts) == 3:
        action, item, target = parts
        if action == "benutze":
            return player.use(item, target)
    return "Unbekannter Befehl."
