# Identity
With the browser cookie being sunset in the next 2 years (if Google ever really decides to do it) it is going to be vital to build in new mechanisms for identifying and segmenting audiences anonymously. This repo will be used to store data analysis exercises around this concept.

## Identity Philosophy
The approach this repo takes is to mimic real-world conditions when identifying PII data on the internet and how to securely store and reidentify PII data later. Below bullet points outline the overall approach and how the approach is intended to achieve the goals of this repo.
- Create a custom module that stores ways to create, anonymize, and analyze FAKE PII datasets. This module is meant to consolidate code on jupyter notebooks and offer a plug and play tool to use in various exercizes and usecases.
- Develop thought experiments designed to analyze and mimic how anonymized data is identified securly and looked up against overlapped datasets.
- Through these thought experiments mimic real world conditions that impact match rate and scale.

# Custom Modules
The below section lists out all of the custom modules used for the various exercises and analysis.

## everyone_anonymous 
The **everyone_anonymous** module is used to store tools and methods for building, analyzing, and modeling anonymous datasets.

### [something_nothing](https://github.com/finnnilsen90/identity/blob/main/everyone_anonymous.py) class 
This class is used to generate fake PII data (not real people) using the below linked CSV of baby names. This class can also hash FAKE email addresses and lookup hashed values in the dataset.

#### Names CSV
The below CSV file is used to generate the FAKE PII. It is simply a list of baby names.
https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

#### Inputs
The something_nothing() class takes in two inputs outlined below. 
- **data** The data input is the below data object. This object is intended to structure the data that will ultimately populate the object.
data = {
            'First_Name': [],
            'Last_Name': [],
            'Email': []
        }

- **nrows** The number of rows in the dataset.

#### Functions
- **something_nothing(data,nrows).generate_data()** generates the fake PII data.
- **something_nothing(data,nrows).hash()** hashes the emails and returns an array of hashed values.
- **something_nothing(data,nrows).match(hashed)** takes in a hashed value and looks it up against the PII dataset. It returns the email that was originally hashed.

### [add_something](https://github.com/finnnilsen90/identity/blob/main/everyone_anonymous.py) class 
Used to build on existing datasets. One example usecase is to create a dataset with the **something_nothing** classes generate_data() function and add PII to that dataset.

#### Inputs
- **data** This is going to be an already formed data object.
- **nrows** The number of rows in the dataset.

#### Functions
- **add_demo_data(gender=True,age=True,hhi=True,gender_scew=50,age_min=18,age_max=80,hhi_scew=800000)** adds demo data to the dataset.

# Thought Experiments
When thinking of ways to anonymously identify users on the internet one of the most important questions to answer is how is scale going to be impacted? The goal of thess thought experiments is to model different hypothetical scenarios and build tools to better answer business questions on this topic.

## [general_thought_experiment](https://github.com/finnnilsen90/identity/blob/identity_v1.1/general_thought_expriment.ipynb)
A 100,000-user dataset with PII from a company called Finn Corp is hashed utilizing the email address. These hashed emails are used by the DSP to identify users that login to a publisher’s website. Determine the scale when targeting those hashed email addresses in a $5,000 display campaign.

### Supply Side Business Questions
- What percent of users login to a publisher website?
- Of those logged in users what percent of them are in our dataset?
### Buy Side Business Questions
- What is the frequency per hashed email over the lifetime of a 30-day digital campaign?
- How much is spent to reach the matched emails with a 4-dollar CPM?

## [overlap_thought_expriment](https://github.com/finnnilsen90/identity/blob/identity_v1.1/overlap_thought_expriment.ipynb)
A 100,000-user dataset with PII from a company called Finn Corp is compared to a 500,000 dataset with PII that includes demographic data. The goal of this overlap analysis is to first see what the % overlap is and second define demographic information.

### Business Questions
- What is the percent overlap between the 2 datasets?
- What is the demographic information of the matched dataset?