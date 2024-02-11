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
import statistics
from collections import Counter

FILENAME = "boston_marathon_2023.csv"
BIB_HEADER = "BibNumber"
AGE_HEADER = "AgeOnRaceDay"
RANK_HEADER = "RankOverall"
GENDER_HEADER = "Gender"
TIME_HEADER = "OfficialTime"
NAME_HEADER = 'FullName'
COUNTRY_HEADER = 'CountryOfResAbbrev'
DIR = "/Users/niambashambu/Desktop/DS 2500/Homeworks/HW 2"

def clean_numeric(s):
    ''' given a string with extra characters $ or , or %, remove them
        and return the value as a float
    '''
    s = s.replace("$", "")
    s = s.replace("%", "")
    s = s.replace(",", "")
    s= s.replace(":", "")
    return float(s)
def clean_data(dct, year_header):
    ''' given a dictionary that includes currency and
        numbers in the form x,xxx, clean them up and convert
        to int/float
    '''
    for key, value in dct.items():
        for i in range(len(value)):
            if not value[i].replace(" ", "").isalpha():
                value[i] = clean_numeric(value[i])
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
    
    #find average time ratings
    '''
    clean_data(dct,TIME_HEADER)
    timesss = dct[TIME_HEADER]
    for i in range(len(timesss)):
        timesss[i] = int(timesss[i])
    
    medtime = median(timesss)
    meantime = sum(timesss)/len(timesss)
    print(f"Median times{medtime}, mean time{meantime}  ")
'''
#How many women finished in the top 1000 in 2021?
    i=0
    gender = dct[GENDER_HEADER]
    for genders in gender:
        
        if genders == "F":
            #print(genders)
            
            i+=1

    #print(i)

    #Apart from the US, which country had the most runners in 2023? Give your answer as the country abbreviation the way it appears in the file (KAZ, THA, ETH, etc.)
    country = dct[COUNTRY_HEADER]
    counter = set([x for x in country if country.count(x) > 1])
   
           
            

    reasons_count = Counter(country)
    most_common_reasons = reasons_count.most_common()
    if len(most_common_reasons) > 1:
        second_most_common_reason = most_common_reasons[1]
        print(f"Second most common country in race: {second_most_common_reason[0:]} ")
            
    
    



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
