import sys
sys.path.append('../parentdirectory')
from table import Table
from parentdirectory.main import seats_all
from parentdirectory.main import seats_names

class Openspace:
    def __init__(self, number_of_tables):
        # Create 6 empty tables and put them in a list
        tables = [Table() for i in range(number_of_tables)]
        self.tables = tables
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
                
"""
    def store(filename):
        #store repartition in .xls
        import pandas as pd
        #example:
        df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
               index=['row 1', 'row 2'],
               columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")
        with open('repartition.xls', 'w') as f:
            f.write(f"Table [counter]: ")
"""
