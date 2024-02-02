


'''
DS 2500
Spring 2024
Code from class - student loan data from one month

Questions to ask/answer:
    - average amount owded per person, overall
    - average amounto wed per person, in a given state
    - state with min/max # borrowers
    - state with min/max total balance
    - average # borrowers over all states
    - average balance over all states
    - correlation between number of borrowers and balance
'''
import pandas as pd
import matplotlib.pyplot as plt
import csv
HEADER =6
FILENAME = "/Users/niambashambu/Desktop/DS 2500/CSV Student Loan Classwork/2016_balances_borrowers.csv"


def read_file(filename):
    #df.drop(index=df.index[0:4], axis=0, inplace=True)
    #print(df)
    data = []
    with open(filename,"r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data



def clean_number(s):
    '''given a string remove, $ and return the float version of the string'''
    s= s.replace(",","")
    s= s.replace("$","")
    return float(s)

def clean_data(lst):
    '''given a 2d list of strings, convert to number wehere apporpriate and return a new 2d list'''
    cleaned=[]
    for row in lst:

        #row[1]=clean_number(row[1])
        #row[2]=clean_number(row[2])
        for i in range(1,len(row)):
            row[i]=clean_number(row[i])
        cleaned.append(row)
    return cleaned

def sum_column(lst,num=0):
    try:
        col = [row[num]for row in lst] #creates a list with the values in specific column
        num_val = [value for value in col if isinstance(value,(int,float))] #filters out non float or int values and gathers all the num values
        return sum(num_val) #returns the sum of the num values
    except TypeError:
        return 0
    except IndexError:
        return 0

def twod_to_dict(lst):
    dct = {}
    for row in lst:
        dct[row[0]]=row[1:]
    return dct

def plot_comparison(value1,state1,value2,state2):
    #create a bar plot that compares the value of two states

    plt.bar([0,1],[value1,value2], color = {"fuchsia","aqua"})
    plt.xlabel("States")
    plt.ylabel("Total Outstanding Balance in Millions")
    plt.title(f"{state1} vs {state2} outstanding student loan balance,2016")
    plt.xticks([0,1],[state1,state2])
    plt.show()

def main():
    #read in the csv file to a 2d list
    # df = pd.read_csv(FILENAME)

    lst = read_file(FILENAME)
    
    #clean the data convert strings to numbers where apporopriate
   # cleaned_data = clean_data(lst[6:])
    cleaned = clean_data(lst[HEADER:])

    # create dictonary version of list
    data_dict = twod_to_dict(cleaned)

    total_borrowers = sum_column(cleaned,1)
    print(f"{round(total_borrowers)} people have student loans in US in 2016")
    
    state1 = input("Which state?\n")
    state2 = input("compared to which other state\n")
   # print(f"{state} has {round(data_dict[state][0])} borrowers")
    #avg_per_borrower = data_dict[state][1]/data_dict[state][0]
    #print(f"{state} has average balance per borrower: ${avg_per_borrower}")
    plot_comparison(data_dict[state1][1],state1,data_dict[state2][1],state2)

if __name__ == "__main__":
    main()