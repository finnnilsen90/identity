import pandas as pd
import numpy as np
import random

# CSV file of baby names to create FAKE PII.
names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
names = [i for i in names['Name']]

# Make something from nothing to test FAKE anonomyzed data. 
class something_nothing:

    def __init__(self,data,nrows):
        self.data = data
        self.nrows = nrows+1
    # Generate a random dataset to represent data with PII.
    def generate_data(self):
        data = self.data

        for i in range(self.nrows):
            rand_first = random.randrange(len(names))
            rand_last = random.randrange(len(names))

            data['First_Name'].append(names[rand_first])
            data['Last_Name'].append(names[rand_last])
            data['Email'].append(data['First_Name'][i]+data['Last_Name'][i]+'@gmail.com')

        return data

    # Hash emails.
    def hash(self):

        df = pd.DataFrame(self.data)
        email_arr = [i for i in df['Email'][1:]]
        hashed = []
        for i in range(len(email_arr)):
            hashed.append(hash(email_arr[i]))

        return hashed

    # Search hashed emails.
    def match(self,hashed):

        df = pd.DataFrame(self.data)
        email_arr = [i for i in df['Email']]
        for i in range(len(email_arr)):
            email = email_arr[i]
            if hash(email) == hashed:
                return email