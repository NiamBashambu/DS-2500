def lst_to_dct(lst):
    dct = {}
    for row in lst:
        dct[row[0]]=row[1:]
    return dct



def col_to_lst(lst,num):
    try:
        col = [row[num]for row in lst] #creates a list with the values in specific column
        num_val = [value for value in col if isinstance(value,(int,float))] #filters out non float or int values and gathers all the num values
        return (num_val) #returns the num values
    except TypeError:
        return 0
    except IndexError:
        return 0
    
def sum_cols(lst):
    col_totals = [ sum(x) for x in zip(*lst) ]
    return(col_totals)

