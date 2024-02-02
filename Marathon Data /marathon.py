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

FILENAME = "/Users/niambashambu/Desktop/DS 2500/Marathon Data /boston_marathon_2022.csv"
BIB_HEADER = "BibNumber"
AGE_HEADER = "AgeOnRaceDay"
RANK_HEADER = "RankOverall"
GENDER_HEADER = "Gender"
TIME_HEADER = "OfficialTime"
NAME_HEADER = 'FullName'
DIR = "files"



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
        if not os.path.isdir(file) and file.endswith(ext):
            filenames.append(dirname + "/"+ file)
    return filenames

def main():
    # Gather data - read in the MBTA speed restrictions as a 2d list
    # and then convert to a dictionary where keys come from the header
    data = read_csv(DIR + '/' +FILENAME)
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
    print(f"{len(names)} finsihers over two years")
    print(f"{len(set(names))} individuals over two years")

   
    
    

if __name__ == "__main__":
    main()
