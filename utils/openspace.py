from random import random
from table.py import Table
from main.py import seats_all
from main.py iport seats_names

class Openspace:
    def __init__(self, number_of_tables):
        # Create 6 empty tables and put them in a list
        self.tables = [Table() for i in range(number_of_tables)]
        self.number_of_tables = number_of_tables
        

    def organize(names_all):
        for table in self.tables:
            while table.has_free_spot():
                table.assign_seat(seat)

        for seat, name in seats_names:
            if seat.free:
                seat.set_occupant(name)

    def display(self):
        print(f"There are {self.number_of_tables} tables, who have {len(seats_all)} seats in total.")
        for table in self.tables:
            counter = 0
            print(f"The occupants of table {counter} are:")
            for seat in self.tables.seats[counter]:
                print(seat.occupant)
            counter += 1 
                

    def store(filename):
        #store repartition in .xls
        """
        with open('repartition.xls', 'w') as f:
            f.write(f"Table [counter]: ")
        """
