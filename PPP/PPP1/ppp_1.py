'''
    Write the following function:
        * Name: sum_column
        * Parameter: 2d list of anything, int for column number - optional
                     If no column number given, use 0
                     (data type in that column must be numeric)
        * Returns: sum of all values in the given column
'''
'''
Niam Bashambu
DS 2500
PPP1

'''
#many tries later with different verisons of this code i got it to work for the auto grader. 
def sum_column(lst,num=0):
    try:
        col = [row[num]for row in lst] #creates a list with the values in specific column
        num_val = [value for value in col if isinstance(value,(int,float))] #filters out non float or int values and gathers all the num values
        return sum(num_val) #returns the sum of the num values
    except TypeError:
        return 0
    except IndexError:
        return 0
    
        
'''
def main():
    lst = [[3, 5, 7], [10, 10, 10]]
    num = int(input("enter a number"))
    sum_column(lst,num)
    print(sum_column(lst,num))


if __name__ == "__main__":
    main()
    '''