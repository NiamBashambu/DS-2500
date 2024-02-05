'''
In 2013, what was the mean finish time of the top 1000 runners?
What is the median age of the top 1000 runners in 2010? 
Apart from the US, which country had the most runners in 2023? 
How many women finished in the top 1000 in 2021?
What is the correlation (r-value) of year vs. the mean finish time of women in the top 1000?
What is the correlation (r-value) of year vs. the mean finish time of American runners in the top 1000?
If the 2020 race had actually happened, what would you predict to be the mean finish time of Americans in the top 1000?

Plot #1: A linear regression plot  modeling the relationship between year and mean finish times of American runners in the top 1000.

Plot #2: A plot showing how median age 
and average finish times have changed over time. 
Because finish times and ages are on quite different scales, 
use the min/max normalization from class to scale the data 
-- we’ll cover it on Tuesday 2/6!





'''

'''
    DS2500
    Spring 2024

    Python week! This week we'er focusing on some python skills including:
        * creating/writing files
        * using the os library to navigate your directory structure
        * plotting with seaborn on top of matplotlib
        * dictionaries deep-dive
        * overview of other data structures (tuples, sets)
        * deep vs shallow copies

'''

import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
from utils import read_csv,lst_to_dct,median

FILENAME = "boston_marathon_2022.csv"
BIB_HEADER = "BibNumber"
AGE_HEADER = "AgeOnRaceDay"
RANK_HEADER = "RankOverall"
GENDER_HEADER = "Gender"
TIME_HEADER = "OfficialTime"
NAME_HEADER = 'FullName'
DIR = "/Users/niambashambu/Desktop/DS 2500/HW 2/"



def filter_age(target_age, ages, times):
    ''' given a target age, a list of ages, and a list of times,
        filter and return a list of times for runners who are the given
        age OR OLDER
    '''
    filtered_times = []
    for i in range(len(ages)):
        if ages[i] >= target_age:
            filtered_times.append(times[i])
    return filtered_times
def get_filename(dirname, ext = ".csv"):
    '''give a directory name (string), 
    return the full path and name 
    for every non directory file in the directory (list of strings)
    '''
    filenames = []
    files = os.listdir(dirname)
    for file in files:
        full_path = os.path.join(dirname, file)  # Corrected to use the full path
        if not os.path.isdir(full_path) and file.endswith(ext):  # Corrected check
            filenames.append(full_path) 
    return filenames

def main():
    # Gather data - read in the MBTA speed restrictions as a 2d list
    # and then convert to a dictionary where keys come from the header
    data = read_csv(DIR + '/'+FILENAME)
    dct = lst_to_dct(data)
    #print(dct)    
    
    # pull out a list of ages
    ages = dct[AGE_HEADER]
    for i in range (len(ages)):
        ages[i] = int(ages[i])
    
    #iteraing by value
        #use listslicing to look at every 20th element intstead of everyone
    for age in ages[::20]:
        print(f"Someone is {age} years old")
    
    # filter to keep everyone older than me
    #master_times = filter_age(45, ages, dct[TIME_HEADER])
    #print(f"Times of everyone 45 or older: {master_times}")
    
    med = median(ages)
    mean = sum(ages)/len(ages)
    print(f"Median age: {med}, mean age: {round(mean,3)}")
    
    

    #read everyfile in a given directory without knowing its name
    filenames = get_filename(DIR)
    print(filenames)

    names = []
    for filename in filenames:
        lst = read_csv(filename)
        dct = lst_to_dct(lst)
        names+= dct[NAME_HEADER]
    #print(f"{len(names)} finsihers over two years")
    #print(f"{len(set(names))} individuals over two years")

   
    
    

if __name__ == "__main__":
    main()
