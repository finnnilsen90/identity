# identtiy
With the browser cookie being sunset in the next 2 years (if Google ever really decides to do it) it is going to be vital to build in new mechanisms for identifying and segmenting audiences anonymously. This repo will be used to store data analysis exercises around this concept.

## Custom Modules
The below section lists out all of the custom modules used for the various excercizes and analysis.

### everyone_anonymouse 
The **everyone_anonymouse** module is used to store tools and methods for analyzing and modeling anonymouse datasets.

#### something_nothing class 
This class is used to generate fake PII data (not real people) using the below linked CSV of baby names. This class can also hash FAKE email addresses and lookup hashed values in the dataset.

##### Names CSV
The below CSV file is used to generate the FAKE PII. It is simply a list of baby names.
'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

##### Inputs
The something_nothing() class takes in two inputs outlined below. 
- **data** The data input is the below data object. This object is intended to structure the data that will ultimately populate the object.
data = {
            'First_Name': [],
            'Last_Name': [],
            'Email': []
        }

- **nrows** The number of rows in the dataset.

##### Functions
- **something_nothing(data,nrows).generate_data()** generates the fake PII data.
- **something_nothing(data,nrows).hash()** hashes the emails and returns an array of hashed values.
- **something_nothing(data,nrows).match(hashed)** takes in a hashed value and looks it up against the PII dataset. It returns the email that was originally hashed.

## Thought Experiments
When thinking of ways to anonymously identify users on the internet one of the most important questions to answer is how is scale going to be impacted? The goal of thess thought experiments is to model different hypothetical scenarios and build tools to better answer business questions on this topic.

### general_thought_experiment
A dataset with PII from a large company called Finn Corp is hashed utilizing the email address. These hashed emails are utilized by the DSP to identify users that login to a publishers website. Determine the scale when targeting those hashed email addresses by answering the following business questions.

#### Supply Side Business Questions
- What percent of users login to a publisher website?
- Of those logged in users what percent of them are in our data set?
#### Buy Side Business Questions
- What is the frequency per hashed email over the lifetime of a 30 day digital campaign?
- How much is spent to reach the matched emails with a 4 dollar CPM?