import pandas as pd
import numpy as np
import random

# CSV file of baby names to create FAKE PII.
names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
names = [i for i in names['Name']]

# Make something from nothing to test FAKE anonomyzed data. 
class something_nothing:

    def __init__(self,data=None,nrows=0):
        self.data = data
        self.nrows = nrows+1
    # Generate a random dataset to represent data with PII.
    def generate_data(self,gender_scew=50,age_min=18,age_max=80,hhi_scew=800000):
        data = self.data
        data_len = self.nrows

        for i in range(data_len):
            
            # Basic PII that should always be included in the dataset.
            rand_first = random.randrange(len(names))
            rand_last = random.randrange(len(names))
            try:
                data['First_Name'].append(names[rand_first])
                data['Last_Name'].append(names[rand_last])
                data['Email'].append(data['First_Name'][i]+data['Last_Name'][i]+'@gmail.com')
            except KeyError as e:
                if data['First_Name'] == e:
                    data['Last_Name'].clear() 
                else:
                    data['First_Name'].clear()
                data = 'Missing a '+str(e)+'. Please add a '+str(e)+' to the dictionary.'
                break

            # Optional PII that may or maynot be included in the dataset.
            create_demo_data = self.demo_data(gender_scew,age_min,age_max,hhi_scew)

            try:
                data['Gender'].append(create_demo_data['Gender'])
                data['Age'].append(create_demo_data['Age'])
                data['HHI'].append(create_demo_data['HHI'])
            except KeyError:
                continue
     
        return data
    
    def demo_data(self,gender_scew,age_min,age_max,hhi_scew):
        
        rand_gender = random.randrange(100)
        if rand_gender > gender_scew:
            gender = 'Male'
        else:
            gender = 'Female'

        rand_age = random.randrange(age_min,age_max)

        rand_hhi = random.randrange(hhi_scew)

        hhi_value = 100000 + hhi_scew

        if rand_hhi < 50000:
            hhi = 'Less than $50,000'
        elif rand_hhi >= 50001 and rand_hhi < 100000:
            hhi = '\$50,001 - $100,000'
        elif rand_hhi >= 100001 and rand_hhi < 200000:
            hhi = '\$100,001 - $200,000'
        elif rand_hhi >= 200001 and rand_hhi < 500000:
            hhi = '\$200,001 - $500,000'
        else:
            hhi = 'More than $500,000'

        demo_obj = {
            'Gender': gender,
            'Age': rand_age,
            'HHI': hhi
        }

        return demo_obj

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

# Add something to nothing to build FAKE PII datasets.

class add_something:

    def __init__(self,data=None,nrows=0):
        self.data = data
        self.nrows = nrows
    
    def add_demo_data(self,gender=True,age=True,hhi=True,gender_scew=50,age_min=18,age_max=80,hhi_scew=800000):
        
        data = self.data

        if gender:
            data.update({'Gender': []})
        if age:
            data.update({'Age': []})
        if hhi:
            data.update({'HHI': []})

        for i in range(self.nrows):
            demo_data = something_nothing().demo_data(gender_scew,age_min,age_max,hhi_scew)
            try:
                data['Gender'].append(demo_data['Gender'])
                data['Age'].append(demo_data['Age'])
                data['HHI'].append(demo_data['HHI'])
            except KeyError:
                continue

        return data