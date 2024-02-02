'''
    Niam Bashambu
    DS2500
    Spring 2024
    
    Starter code for working with the MBTA data -- speed restrctions
    
    We have for starter code:
        * constants for the name of the file, and some of the headers
          we care about
        * read_csv to read the CSV file and return a 2d list
        
    Privacy/ethical concerns about the data:
        * Provided by the MBTA itself
        * None of it is personal or identifiable
        * Some if it might be out-of-date
        * They're incentivized to lie, but face big consequences
    
'''

import csv
import statistics
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()

MBTA_FILE = "/Users/niambashambu/Desktop/DS 2500/MBTA Transit Info/speed_restrictions.csv"
SPEED_HEADER = "Restriction_Speed_MPH"
DISTANCE_HEADER = "Restriction_Distance_Feet"
LINE_HEADER = "Line"
PRI_HEADER = "Priority"
PRI_NAMES = ["LOW", "MED", "HIGH"]
LINE_NAMES = ["Green", "Red", "Orange", "Blue"]
REASON_HEADER = "Restriction_Reason"

def read_csv(filename):
    ''' given the name of a csv file, return its contents as a 2d list,
        including the header.'''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data
''' dct = {}
    for row in lst:
        dct[row[0]]=row[1:]
    return dct'''

def lst_to_dct(lst):
    dct = {}
   
    
    for header in lst[0]:
        dct[header]= []
    for row in lst[1:]:
        for i in range(len(row)):
            dct[lst[0][i]].append(row[i])
    return dct

def filter_line(s, lst,lst2):
    #find the instances in the first list where the value of s corresponds to the line in lst.
    #then uses the second list parameter to figure out the corresponding numbers to print out
    s_lower = s.lower()
    #creating a new lst to store the sorted values of the second lst. 
    newlst=[]
    #zipping together the corresponding line with the value
    for x,z in zip(lst,lst2):
        

        #making sure that the value of what line is in the zipped up lsts. 
        if s_lower in x.lower():
            #adding the value corresponding to the correct line to the new lst
            newlst.append(z)
    #returning the new list
    return newlst

def convert_mph(s):
    '''given a string of the form xx MPH, return just the numeric part as an int'''
    mph = s.split()[0]
    return int(mph)

    



def main():
    # read in the speed restrictions data into a 2d list
    data = read_csv(MBTA_FILE)

    #want to compute the median distance(feet)
    #and mean distance in (feet)

    data_dct = lst_to_dct(data)
    print(data_dct)


    #convert feet from strings to ints
    feet = [int(item) for item in data_dct[DISTANCE_HEADER]]
    
    mean_feet = sum(feet) / len(feet)
    print(f"mean distance in feet: {round(mean_feet,3)}")


    med_feet = statistics.median(feet)
    print(f"median distance in feet:{med_feet}")


    most_restrictions = statistics.mode(data_dct[LINE_HEADER])
    
    print((f"{most_restrictions} has the most restrictions"))
    
    #get most common reason for restricitons
    reason_restrictions = statistics.mode(data_dct[REASON_HEADER])
    
    print(reason_restrictions)
    #find reasons for restrictions
    counter = set([x for x in data_dct[REASON_HEADER] if data_dct[REASON_HEADER].count(x) > 1])
    print(counter)

    #get the mean distance of restriictions on green line
    green_dist = filter_line("green", data_dct[LINE_HEADER],feet)
    print(green_dist)
    mean_green = sum(green_dist)/len(green_dist)
    print(f"Mean disctance on the green line is {mean_green} feet")

    #find the line with the most track under restrction
    #correlation between distance and mph -- overall and for indiviudual lines
    #if we find a strong correlation, we can do a linear regression

    #print(data_dct[SPEED_HEADER])

    #clean up and convert our MPH in to ints "x mph" -- x
    #mph = [convert_mph(item) for item in data_dct[SPEED_HEADER]]

    #print(mph)
    mph = []
    for item in data_dct[SPEED_HEADER]:
        mph.append(convert_mph(item))

    print(mph)
    #median speed restriction
    med_mph = statistics.median(mph)
    print(med_mph)
    

    #find orange line median restirions
    orange_dist = filter_line("orange", data_dct[LINE_HEADER],mph)
    print(orange_dist)
    orange_dist_sorted = sorted(orange_dist)
    orange_dist_med=statistics.median(orange_dist_sorted)
    print(orange_dist_med)

    
    # what is the correlation between feet and mph?
    corr = statistics.correlation(feet,mph)
    print(f"correlation between feet,mph: {corr}")
    

    #what is the correlation between fet and mph on individual lines?

    for line in LINE_NAMES:
        line_dist = filter_line(line,data_dct[LINE_HEADER],feet)
        line_mph = filter_line(line,data_dct[LINE_HEADER],mph)
        #make sure both lists aren't empty
        if line_dist and line_mph:
            corr = statistics.correlation(line_dist,line_mph)
            print(f"{line} correlation: {corr}")



    #we have a decent correlation on the green line 
    #try a linear regression
    
    green_mph = filter_line("green",data_dct[LINE_HEADER],mph)
    lr = stats.linregress(green_dist,green_mph)
    
    #given an x value compute the y value using y =mx+b

    x = int(input("enter a lengh of a restricion in feet\n"))
    y = lr.slope *x + lr.intercept
    print(f"the mph on that length of trak owuld be ... {y}")

    #visualize the line of best fit for the green line
   # sns.regplot(x= green_dist,y=green_mph)
    #plt.show()
    
    
if __name__ == "__main__":
    main()