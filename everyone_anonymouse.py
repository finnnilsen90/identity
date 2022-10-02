import pandas as pd
import numpy as np
import random

names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
names = [i for i in names['Name']]

# Make something from nothing. Generate a random dataset to represent data with PII.
class something_nothing:

    def __init__(self,data,nrows):
        self.data = data
        self.nrows = nrows
    
    def generate_data(self):
        data = self.data

        for i in range(self.nrows):
            rand_first = random.randrange(len(names))
            rand_last = random.randrange(len(names))

            data['First_Name'].append(names[rand_first])
            data['Last_Name'].append(names[rand_last])
            data['Email'].append(data['First_Name'][i]+data['Last_Name'][i]+'@gmail.com')

        return data

    def hash(self):

        arr = self.data['Email']
        hashed = []
        for i in arr:
            hashed.append(hash(i))

        return hashed

    def match(self,hashed,data):

        for i in range(len(data)):
            email = data['Email'][i]
            if hash(email) == hashed:
                return email
            







