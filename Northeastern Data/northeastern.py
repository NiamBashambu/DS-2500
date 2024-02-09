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

from utils import get_filename, read_csv, lst_to_dct, normalize, moving_avg

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
def plot_lines(x, ys, labels):
    ''' given a list of x values, a 2d list of y values, and a
        corresponding list of labels (strings)
        plot all the ys against the same list of x's
    '''
    for i in range(len(ys)):
        sns.lineplot(x = x, y = ys[i], label = labels[i])
    plt.show()



def main():
    #set up system path to look for utils
    sys.path.insert(0,"../utils")

    #open all files from my data directory
    filenames = get_filename(DIRECTORY)
    print(filenames)
    data_dct = {}
    for file in filenames:
        data = read_csv(file)
        if "demographics" in file:
            demo_header = data[0][1:]
        dct = lst_to_dct(data)
        #concatinate function for dictonaries
        data_dct = {**data_dct,**dct}
    


    #clean up data to get the rid of random symbols

    clean_data(data_dct, YEAR_HEADER)
    '''
    #plot tuition vs admission rate
    plot_lines(data_dct[YEAR_HEADER], [data_dct[TUITION_HEADER], 
                                      data_dct[ADM_HEADER]],
               ["Tuition", "Admission Rate"])
    
    
    # normalize tuition/admission values, and try again
    normal_tuition = normalize(data_dct[TUITION_HEADER])
    normal_adm = normalize(data_dct[ADM_HEADER])
    plot_lines(data_dct[YEAR_HEADER], [normal_tuition, normal_adm],
               ["Tuition", "Admission Rate"])
    '''

    #demographics info
    for demo in demo_header:
        sns.lineplot(data= data_dct, x = YEAR_HEADER, y = demo)
        mvg = moving_avg(data_dct[demo])
        sns.lineplot(x = data_dct[YEAR_HEADER][1:], y = mvg,color = "pink")
        plt.title(demo)
        plt.show()
        

        #what is the mean of the demographic info

        mean = sum(data_dct[demo]) / len(data_dct[demo])
        print(f"Mean of {demo}: {mean}")
        stddev = statistics.stdev(data_dct[demo])
        print(f"Std dev:{stddev}\n")
        

if __name__ == "__main__":
    main()
