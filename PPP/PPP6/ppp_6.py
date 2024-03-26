'''
Filename: ppp_6.py

Write the following function:
* name: compute_centroids
* parameters: a dataframe that has at least the following columns:   
              "cluster", "x", "y", and a k for num clusters
* returns: a list of tuples with average (x, y) values for each 
     cluster
For example...
Given 
cluster      x     y
            0            3     4,
1

      Your function should return [(3, 4)]

Given 
cluster      x     y
            0            3     4
            0            5     1,
1      

      Your function should return [(4, 2.5)]

Given 
cluster      x     y
            0            3     4
            0            5     1    
            1            3     4 ,
2 

      Your function should return [(4, 2.5), (3, 4)]


You can assume that clusters are numbered 0, 1, ..., k-1.



'''