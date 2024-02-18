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
from utils import read_csv,lst_to_dct,median,normalize
import statistics
from collections import Counter
from datetime import datetime

from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import numpy as np



FILENAME = "boston_marathon_2010.csv"
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

def calculate_mean_finish_time(times):
    '''Given a list of finish times in HH:MM:SS format, calculate the mean finish time in seconds.
    same as the code as before'''
    z = []
    for time in times:
        pt = datetime.strptime(time,'%H:%M:%S')
        total_seconds = pt.second + pt.minute*60 + pt.hour*3600
        z.append(total_seconds)

    meantime = sum(z)/len(z)
    return meantime

def get_subgroup_data(directory, gender=None, country=None):
    '''Given a directory of CSV files, filter data by gender and/or country and calculate mean finish times per year.'''
    filenames = get_filename(directory, ".csv")
    years = []
    mean_finish_times = []
    for filename in filenames:
        year = filename.split("_")[-1].split(".csv")[0]  
        data = read_csv(filename)
        dct = lst_to_dct(data)
        times = dct[TIME_HEADER]

        if gender:
            times = [dct[TIME_HEADER][i] for i in range(len(dct[GENDER_HEADER])) if dct[GENDER_HEADER][i] == gender]
        if country:
            times = [dct[TIME_HEADER][i] for i in range(len(dct[COUNTRY_HEADER])) if dct[COUNTRY_HEADER][i] == country]

        mean_time = calculate_mean_finish_time(times)
        years.append(int(year))
        mean_finish_times.append(mean_time)

    return years, mean_finish_times

def plot_lines(x, ys, labels):
    ''' given a list of x values, a 2d list of y values, and a
        corresponding list of labels (strings)
        plot all the ys against the same list of x's
    '''
    for i in range(len(ys)):
        sns.lineplot(x = x, y = ys[i], label = labels[i])
    plt.show()



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
    #for age in ages[::20]:
    #    print(f"Someone is {age} years old")
    
    # filter to keep everyone older than me
    #master_times = filter_age(45, ages, dct[TIME_HEADER])
    #print(f"Times of everyone 45 or older: {master_times}")
    
    #med = median(ages)
    #mean = sum(ages)/len(ages)
    #print(f"Median age: {med}, mean age: {round(mean,3)}")
    
    #find average time ratings
    
    
    timesss = dct[TIME_HEADER]
    z = []
    for time in timesss:
        pt = datetime.strptime(time,'%H:%M:%S')
        total_seconds = pt.second + pt.minute*60 + pt.hour*3600
        z.append(total_seconds)
        
    
    
    meantime = sum(z)/len(z)
    print(f" mean time{meantime}  ")

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
            
    


    '''
    #read everyfile in a given directory without knowing its name
    filenames = get_filename(DIR)
    #print(filenames)

    names = []
    for filename in filenames:
        lst = read_csv(filename)
        dct = lst_to_dct(lst)
        names+= dct[NAME_HEADER]
        '''
    #print(f"{len(names)} finsihers over two years")
    #print(f"{len(set(names))} individuals over two years")
        
    # getting the data using function above
    years_women, mean_times_women = get_subgroup_data(DIR, gender="F")
    years_us, mean_times_us = get_subgroup_data(DIR, country="USA")

# Calculate correlation (r-value)#used stack overflow to learn what pearsonr was and how to use it
    r_value_women,_= pearsonr(years_women, mean_times_women)
    r_value_us,_ = pearsonr(years_us, mean_times_us)

    print(f"Correlation of year vs. mean finish time for women: {r_value_women}")
    print(f"Correlation of year vs. mean finish time for American runners: {r_value_us}")

#the 2020 problem #used a lot of outside help for this
    years_us = np.array(years_us).reshape(-1, 1)  # Reshape for sklearn
    mean_times_us = np.array(mean_times_us)

# Fit linear regression model
    model = LinearRegression().fit(years_us, mean_times_us)

# Predict for 2020
    predicted_time_2020 = model.predict(np.array([[2020]]))[0]

# Convert predicted time from seconds back to the normal time thing
    #used stack overflow to figure out a bit of this
    hours, remainder = divmod(predicted_time_2020, 3600)
    minutes, seconds = divmod(remainder, 60)

    predicted_time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    print(f"Predicted mean finish time for Americans in 2020: {predicted_time_str}")

# Plot #1: Linear regression plot for year vs. mean finish times of American runners
 
    
    # Create linear regression object
    regmodel = LinearRegression().fit(years_us, mean_times_us)

    
    # Make predictions
    mean_finish_times_pred = regmodel.predict(years_us)

    #ploting it
    plt.figure(figsize=(10, 6))
    sns.regplot( x= years_us, y= mean_times_us, ci=None, label='Actual Mean Finish Times')
    plt.plot( years_us, mean_finish_times_pred, color='blue',label='Linear Regression Line')

    plt.xlabel('Year')
    plt.ylabel('Mean Finish Time (seconds)')
    plt.title('Year vs. Mean Finish Times of American Runners')
    plt.legend()
    plt.show()
'''
# Plot #2: Normalized median age and average finish times over time
    average_finish_times= get_subgroup_data(DIR)
    #median_ages = 
    #median_ages_normalized = normalize(median_ages)
    average_finish_times_normalized = normalize(average_finish_times)

# Re-plotting with custom normalization
    plt.figure(figsize=(10, 6))

    #plt.plot(years_us, median_ages_normalized, label='Normalized Median Ages', marker='o')
    plt.plot(years_us, average_finish_times_normalized, label='Normalized Average Finish Times', marker='x')

    plt.xlabel('Year')
    plt.ylabel('Normalized Values')
    plt.title('Changes in Median Age and Average Finish Times Over Time (Custom Normalized)')
    plt.legend()
    plt.show()
   
    '''
    

if __name__ == "__main__":
    main()
