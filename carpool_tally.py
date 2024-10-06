import pandas as pd
import numpy as np
import sys

#----- Define the Person class -----#
class Person:
    '''
    A Person class, which will store how much each person owes/should get
    '''
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def driver(self, trip_cost):
            self.balance -= trip_cost

    def rider(self, trip_cost, num_people):
            self.balance += trip_cost/num_people

#----- Read the tab delimited .txt file -----#
def read_data(file):
    '''
    Read the data in a .txt format. The data should look like:
    DriverName   Passenger1Name   Passenger2Name   ...
    DriverName   Passenger1Name   Passenger2Name   Passenger3Name   ...
    DriverName   Passenger1Name   ...
    Where the drivers name goes first followed by all the passengers that rode with the driver for that day
    All entries should be separated by a tab
    '''
    carpool_data = pd.read_csv((file), sep='\t', header=None)
    return carpool_data
    
#----- Instantiating/creating object for each person that appears in our file -----#
def create_person_objects(data):
    unique_names = pd.unique(data.dropna().values.reshape(-1))
    Person_objects = {name: Person(name) for name in unique_names}
    return(Person_objects)
    
#----- Performing calculation -----#
def calculate(data, trip_cost):
    data = read_data(data)
    people = create_person_objects(data)

    for index, row in data.iterrows():
        '''
        Parse through row by row (so each iteration is 1 trip). 
        Collect who the driver is and who the passengers are
        Calculate the total number of people
        '''
        driver = row[0]
        passengers = row[1:].dropna().values
        total_people = len(row[0:].dropna().values)

        '''
        Update everybody's balances
        '''
        people[driver].driver(trip_cost)
        people[driver].rider(trip_cost, total_people)
        for rider in passengers:
            people[rider].rider(trip_cost, total_people)

    for name, person in people.items():
        print(person.name, "has a balance of",person.balance)

#----- Help statement -----#
def print_help():
    print('''
        Thanks for using my carpool cost calculator
        
        For an example of the usage, please consult the Github repository's README.md:
        https://github.com/joesphbeller/carpool_tally

        syntax: 
        python3 carpool_tally.py filename trip_cost
        
        float trip_cost: Cost of the daily commute
        string filename: The name of the tab delimited file that has the carpool logs  
        ''')

if __name__=="__main__":
    
    if(sys.argv[1]=="-h"):
        print_help()
        
    else:
        filename = sys.argv[1]
        trip_cost = float(sys.argv[2])
        calculate(filename, trip_cost)
