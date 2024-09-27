class Seat:
    def __init__(self, free, occupant):
        self.free = True
        self.occupant = ""
        
    def set_occupant(self, name):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        self.free = True
        self.occupant = ""

class Table():
    def __str__(self):
        return "test"

    def __init__(self):
        self.capacity = 4
        self.seats = []
        tables_all.append(self)

    def has_free_spot(self):
        return self.capacity > len(self.seats)

    def assign_seat(self, seat):
        self.seats.append(seat)

    def left_capacity(self):
        return self.capacity - len(self.seats)

maarten = Seat(True, "Maarten")
tafel_1 = Table()
tafel_1.assign_seat(maarten)
print(maarten)
