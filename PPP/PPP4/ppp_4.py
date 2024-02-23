'''
ppp_4.py
    (note that you need to submit a .py file here, not a notebook!)

Write the following function:
* name: mse
* parameters: two lists of numbers of equal length, one is predicted 
  values and one is actual values
* returns: The Mean Square Error: average of (predicted -
actual)2 for every predicted/actual pair

For example...
Given [1, 2], [3, 4], your function should return 4
Given [0, 0], [1, 5], your function should return 13
Given [1, 1, 1], [1, 5, 10], your function should return 32.333

You can assume that both lists contain numeric values, and are of equal length.


'''


def mse(predicted,actual):
    x_error = []
    for p,a in zip(predicted,actual):
        
        x= ((p - a)**2)
        x_error.append(x)
        
    mean_square_error = sum(x_error)/len(x_error)
        
    return mean_square_error
       