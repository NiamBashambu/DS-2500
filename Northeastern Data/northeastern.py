'''
    DS2500
    Spring 2024
    Week 5 - code from class
    
    Data for this week:
        * Info about northeastern over the last several years
        * For 2013-2021, we have: Selectiveness Rating, Admission Rate,
            % of admitted students w/identity markers, tuition
    
    Starter code for Tuesday:
        * Read in data from several files about the last few years at NEU
        * Files live in a directory named data
        * (optional, put utils.py in another location and udpate system path
           that way you don't need to copy/move the file to your current dir)
        * Has functions to clean the data -- has $ and % and , mixed in nums
    
    During the lecture part, we'll cover
        * Time series data overview
        * Normalizing/scaling data
        * Moving average
    
    And then we'll code that stuff into this starter code. We want to learn
    and visaulize, in particular, tuition vs admission rates, and demographics.
        
'''

import csv
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import sys

from utils import get_filename, read_csv, lst_to_dct

DIRECTORY = "/Users/niambashambu/Desktop/DS 2500/Northeastern Data/data"
YEAR_HEADER = "Year"
TUITION_HEADER = "Living On Campus"
ADM_HEADER = "Admission Rate (Total)"

                       
def clean_numeric(s):
    ''' given a string with extra characters $ or , or %, remove them
        and return the value as a float
    '''
    s = s.replace("$", "")
    s = s.replace("%", "")
    s = s.replace(",", "")
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
    
def normalize(lst):
    '''
    given a list of numbers, return a list of min/max normalized values
    
    '''
    mn = min(lst)
    mx = max(lst)
    normal = []
    for x in lst:
        normal_x = (x-mn)/(mx-mn)
        normal.append(normal_x)
    return normal

def main():
    #set up system path to look for utils
    sys.path.insert(0,"../utils")

    #open all files from my data directory
    filenames = get_filename(DIRECTORY)
    print(filenames)
    data_dct = {}
    for file in filenames:
        data = read_csv(file)
        dct = lst_to_dct(data)
        #concatinate function for dictonaries
        data_dct = {**data_dct,**dct}
    print(data_dct)


    #clean up data to get the rid of random symbols

    clean_data(data_dct, YEAR_HEADER)
    #plot tuition vs admission rate
    sns.lineplot(x = data_dct[YEAR_HEADER],y = data_dct[TUITION_HEADER],label = "Tuition")

    sns.lineplot(x = data_dct[YEAR_HEADER], y = data_dct[ADM_HEADER],label = "admission rate")
    
    plt.show()

    #not reflective of actual admission rate
    #normalize data
    normalized_tui = normalize(data_dct[TUITION_HEADER])
    normalized_adm = normalize(data_dct[ADM_HEADER])
    
    sns.lineplot(x = data_dct[YEAR_HEADER], y = normalized_tui,label = "tuition")
    sns.lineplot(x = data_dct[YEAR_HEADER], y = normalized_adm, label = "admission")
    plt.show()

if __name__ == "__main__":
    main()
