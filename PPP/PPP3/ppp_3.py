'''
Filename: ppp_3.py

Write the following function:
* name: moving_avg
* parameters: list of numbers, optionally an int (the window for the   
              moving average, default to 2)
* returns: a new list, containing the moving average values of the
           original, according to the given window

For example...
Given [7, 5, 4, 10, 12, 3], 2, your function should return [6, 4.5, 7, 11, 7.5]
Given [7, 5, 4, 10, 12, 3], your function should return [6, 4.5, 7, 11, 7.5]
Given [1, 1, 1], 3, your function should return [1]
Given [1, 1, 1], 1, your function should return [1, 1, 1]

You can assume that the window value will be a “reasonable” integer, i.e., at least 1 and no larger than the list’s length.



'''
#fucntion call with the two parameters, one default
def moving_avg(lst,num=2):
    #creating new list for which to append the new values onto
    newlst = []
    #range is the leng of list minus the value of which numbers to average by + 1
    for i in range(len(lst)- num+1):
        #finding the sum of the terms in the num value
        num_sum = sum(lst[i:i+num])
        #findung the average
        num_avg = num_sum/num
        #adding new value to the list
        newlst.append(num_avg)

    return newlst
        
            



