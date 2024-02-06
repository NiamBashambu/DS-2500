
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


def lst_to_dct(lst):
    dct = {}
   
    
    for header in lst[0]:
        dct[header]= []
    for row in lst[1:]:
        for i in range(len(row)):
            dct[lst[0][i]].append(row[i])
    return dct

def median(orig_lst):
    ''' given a list of numbers, compute and return median'''
    lst = orig_lst.copy()
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 == 1:
        return lst[mid]
    else:
        avg = (lst[mid] + lst[mid - 1]) / 2
        return avg

