from utils.table import Table, Seat
from utils.openspace import Openspace
import random
"""
# Import name data and randomize
filename = "./new_collegues.csv"
with open(filename, "r") as f:
    data = f(read)
    file_imported = [data.split()]
#print(file_imported)
#names_imported = del file.imported[:23]
"""

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


names_imported = ["Adheeba","Anastasiia", "Basma", "Dhrisya", "Ihor", "Izabela", 
                    "Kelli", "Kevin", "Levin", "Maarten", "Majid", "Minh Duc", "Moustafa", 
                    "Muntadher", "Nicolaas", "Petra", "Rasmita", "Rik", "Soha", "Tom", 
                    "Urson", "Veena", "Wouter", "Yeliz"]
names_all = random.shuffle(names_imported)

# Create 24 empty seats and put them in a list
seats_all = [Seat(True, "occupant") for i in range(23)]

# Combine both lists as key-value pairs in a dictionary
seats_names = dict(zip(seats_all, names_all))
"""
            func: assign leader
            func: more/less occupants
"""

# Launch
configuration_1 = Openspace.organize(names_all)
configuration_1.display()




