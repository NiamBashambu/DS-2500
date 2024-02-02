
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt

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
