import table.py
import openspace.py
import random

names_imported = ["Adheeba","Anastasiia", "Basma", "Dhrisya", "Ihor", "Izabela", 
                    "Kelli", "Kevin", "Levin", "Maarten", "Majid", "Minh Duc", "Moustafa", 
                    "Muntadher", "Nicolaas", "Petra", "Rasmita", "Rik", "Soha", "Tom", 
                    "Urson", "Veena", "Wouter", "Yeliz"]
names_all = random.shuffle(

# Create 24 empty seats and put them in a list
seats_all = [Seat() for i in range(23)]

# Combine both lists as key-value pairs in a dictionary
seats_names = dict(zip(seats_all, names_all))







