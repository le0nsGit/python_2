
import csv
from collections import Counter



#attributes

#creates list to hold states
state_list = []
#creates list of  the number of shootings
total_shootings_per_state_list = []
a_list = []



#creates list of  the shootings by race
shootings_by_race_list= []


#functions/methods
def intro():
    """
    Presents intro to user.
    """
    # prints intro
    print("\nThis program prints stats on mass shootings in the US by state, sex and race from 2012 to 2014.", end='\n\n')

def open_csv_file():
        # opens file reader to read files
    with open(r'D:\ccac\python_2\us_shooting_deaths_2012_to_2014\mass_shootings.csv', 'r') as csv_file:

        # reads csv file and adds to reader
        csv_reader = csv.DictReader(csv_file)

        for x in csv_reader:
            a_list.append(x)

        return a_list
        
def open_csv():

        # opens file reader to read files
    with open(r'D:\ccac\python_2\us_shooting_deaths_2012_to_2014\mass_shootings.csv', 'r') as csv_file:

        # reads csv file and adds to reader
        csv_reader = csv.DictReader(csv_file)

   
    
        #creates count var and set to 0
        male_count = 0
        female_count = 0
    
    #     loops through each row in file reader
        for row in csv_reader:

            #adds state to list
            state_list.append(row.get('STATE'))

            # adds to shootings by race list
            shootings_by_race_list.append(row.get('RACE'))

            #if male add 1 to count
            if row.get('GENDER') == "Male":
            # if row['GENDER'] == "Male":
                male_count +=1

            # if female add 1 to count
            elif row.get('GENDER') == "Female":
                female_count +=1

        #prints total male mass shootings
        print(f'Mass Shootings by men: {male_count}')

        #prints total female mass shootings
        print(f'Mass Shootings by women: {female_count}\n')

        #counts duplicate mass shootings and adds to dictionary
        states_dict = Counter(state_list)

        #counts duplicate mass shootings by raceand adds to dictionary
        race_dict = Counter(shootings_by_race_list)

    # loops through list of states   
        for state, total_shootings in states_dict.items():

            #prints states and to shootings in that state
            print(f'States: {state}\nTotal Shootings: {total_shootings}\n')

    #prints state with the highest mass shootings
        print(f'\nState with the highest mass shootings: {max(states_dict, key=states_dict.get)}')

    #loops through race dictionary and prints results
        print('\n' f'Mass Shootings by Race:''\n')

        for race, num in race_dict.items():

            #prints results
            print(f'Race: {race}\nTotal Shootings by Race: {num}\n')    




if __name__ == "__main__":

    intro() 
    # open_csv()
    c =  open_csv_file()
    
    print(c)