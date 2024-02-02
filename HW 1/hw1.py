import matplotlib.pyplot as plt
import seaborn as sns
import csv
HEADER =6
FILENAME = "/Users/niambashambu/Desktop/DS 2500/HW 1/num_borrowers_per_state.csv"
FILENAME2= "/Users/niambashambu/Desktop/DS 2500/HW 1/total_loans_per_state.csv"


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
    
def sum_cols(lst):
    col_totals = [ sum(x) for x in zip(*lst) ]
    return(col_totals)



def twod_to_dict(lst):
    dct = {}
    for row in lst:
        dct[row[0]]=row[1:]
    return dct
'''
def plot_comparison(value1,state1,value2,state2):
    #create a bar plot that compares the value of two states

    plt.bar([0,1],[value1,value2], color = {"fuchsia","aqua"})
    plt.xlabel("States")
    plt.ylabel("Total Outstanding Balance in Millions")
    plt.title(f"{state1} vs {state2} outstanding student loan balance,2016")
    plt.xticks([0,1],[state1,state2])
    plt.show()
'''
def plot_histogram_average_balance_2021(cleaned, cleaned2):
    # Calculate average balance per borrower for each state in 2021
    avg_balances_2021 = [(sum(cleaned2[i][-1] for i in range(len(cleaned2))) / sum(cleaned[i][-1] for i in range(len(cleaned)))) * 1e6 for i in range(len(cleaned))]

    
    plt.figure()
    plt.hist(avg_balances_2021, bins=10, color='blue', alpha=0.7)
    plt.title('Average Outstanding Balance per Borrower in 2021')
    plt.xlabel('Average Outstanding Balance ($)')
    plt.ylabel('Number of States')
    plt.show()

def plot_line_chart_balance_over_time(cleaned2, state1, state2):


    
    # Extract balance data for the two selected states
    state1_balances = [row for row in cleaned2 if row[0] == state1][0][1:]
    state2_balances = [row for row in cleaned2 if row[0] == state2][0][1:]

    years = [2016, 2017, 2018, 2019, 2020, 2020, 2021]

    plt.figure()
    plt.plot(years, state1_balances, label=state1, marker='o')
    plt.plot(years, state2_balances, label=state2, marker='o')
    plt.title(f'Average Outstanding Balance Over Time: {state1} vs {state2}')
    plt.xlabel('Year')
    plt.ylabel('Average Outstanding Balance (in millions)')
    plt.legend()
    plt.show()

def main():
    #read in the csv file to a 2d list
    # df = pd.read_csv(FILENAME)

    lst = read_file(FILENAME)
    lst2 = read_file(FILENAME2)
    
    #clean the data convert strings to numbers where apporopriate
   # cleaned_data = clean_data(lst[6:])
    cleaned = clean_data(lst[HEADER:])
    cleaned2 = clean_data(lst2[HEADER:])

    data_dict = twod_to_dict(cleaned)
    data_dict2 = twod_to_dict(cleaned2)
    #print(cleaned)
    # create dictonary version of list
    #data_dict = twod_to_dict(cleaned)
    #How many borrowers had student loans in 2019?
    borrowers_2019 = 0
    for row in cleaned:
        borrowers_2019 += row[4]   
    print(f"Number of borrowers in 2019: {borrowers_2019}")

     # What is the total outstanding balance for all students as of 2021?
    total_balance_2021=0
    for row in cleaned:
        total_balance_2021 += row[7]*1e6
    print(f"Total outstanding balance in 2021: ${total_balance_2021}")

    # What is the average outstanding balance per student in 2016?
    total_balance_2016=0
    borrowers_2016=0
    for row in cleaned2:
        total_balance_2016 +=row[1]*1e6
    for row in cleaned:
        borrowers_2016+=row[1]
    avg_balance_2016 = total_balance_2016 / borrowers_2016
    print(f"Average outstanding balance per student in 20: ${avg_balance_2016:.2f}")

    # What is the average outstanding balance per student in 2021?
    total_balance_2021=0
    borrowers_2021=0
    for row in cleaned2:
        total_balance_2021 +=row[7]*1e6
    for row in cleaned:
        borrowers_2021+=row[7]
    avg_balance_2021 = total_balance_2021 / borrowers_2021
    print(f"Average outstanding balance per student in 2021: ${avg_balance_2021:.2f}")

    # What is Nevada’s average outstanding balance over all years in the dataset?
    nevada_balances = [year_data for state, year_data in data_dict2.items() if state == 'Nevada'][0]
    nevada_avg_balance = sum(nevada_balances) / len(nevada_balances) * 1e6  # Convert to actual value
    print(f"Nevada's average outstanding balance: ${nevada_avg_balance:.2f}")

    # Which state had the greatest balance on average over all years in the dataset, and how much was it?
        #find the greatest average balance state over all the years 
    max_avg_state = max(data_dict2, key=lambda state: sum(data_dict2[state]) / len(data_dict2[state]))
        #finds the average blanace for the state with the greatest balance
    max_avg_balance = sum(data_dict2[max_avg_state]) / len(data_dict2[max_avg_state]) * 1e6  # Convert to actual value
    print(f"State with the greatest average balance: {max_avg_state} (${max_avg_balance:.2f})")

    # Which state had the lowest balance on average over all years in the dataset, and how much was it?
        #find the lowest average balance state overall the years
    min_avg_state = min(data_dict2, key=lambda state: sum(data_dict2[state]) / len(data_dict2[state]))
        #calcualtes the average balance for that state
    min_avg_balance = sum(data_dict2[min_avg_state]) / len(data_dict2[min_avg_state]) * 1e6  # Convert to actual value
    print(f"State with the lowest average balance: {min_avg_state} (${min_avg_balance:.2f})")
    
    #On average, how much did the number of borrowers in a given state change per year? (Assume that, in the first year, the number of borrowers did not change. Compute your first value as the change from 2016 to 2017. Negatives/positives don’t matter here. Going from 10 borrowers to 11, or from 10 to 9, is a change of 1 person.)
    changes_per_state = {state: [abs(year_data[i+1] - year_data[i]) for i in range(len(year_data) - 1)] for state, year_data in data_dict.items()}
    avg_changes = {state: sum(changes) / len(changes) for state, changes in changes_per_state.items()}
    total_avg_change = sum(avg_changes.values()) / len(avg_changes)
    print(f"Average yearly change in number of borrowers: {total_avg_change:.2f}")

    # Plot #1: Histogram of average outstanding balance per borrower in each state, in 2021
    plot_histogram_average_balance_2021(cleaned, cleaned2)

    # Plot #2: Line chart of average outstanding balance per borrower over time for two states
    plot_line_chart_balance_over_time(cleaned2, "California", "Wyoming") 

    
'''

'''
if __name__ == "__main__":
    main()




    '''
Answer these questions (make sure you compute these answers in your Python solution):
How many borrowers had student loans in 2019? - 43988600
What is the total outstanding balance for all students as of 2021? - 10303897
What is the average outstanding balance per student in 2016? - 29526.07
What is Nevada’s average outstanding balance over all years in the dataset? 
Which state had the greatest balance on average over all years in the dataset, and how much was it?
Which state had the lowest balance on average over all years in the dataset, and how much was it?
On average, how much did the number of borrowers in a given state change per year? (Assume that, in the first year, the number of borrowers did not change. Compute your first value as the change from 2016 to 2017. Negatives/positives don’t matter here. Going from 10 borrowers to 11, or from 10 to 9, is a change of 1 person.)

    in Pennsylvania it was 21,716

'''
