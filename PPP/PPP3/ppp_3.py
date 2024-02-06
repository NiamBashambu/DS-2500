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

def moving_avg(lst,num=2):
    return 