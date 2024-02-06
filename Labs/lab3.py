
import os

def sum_distinct(tple):
    '''
    Write a function that, given a list of tuples, modifies the list to contain the sum of distinct elements in each tuple.

Here are the specs:
Function name: sum_distinct
Parameters: list of tuples (numeric values)
Returns: nothing (modifies the list)

Examples of calling your function:
sum_distinct([(1, 1, 2), (3, 5, 6, 5)]) ..... returns nothing but modifies the list to contain [3, 14]
sum_distinct([(1, 1), (5, 5, 5)]) ..... returns nothing but modifies the list to contain [1, 5]

    
    
    '''

    for i,j in enumerate(tple):
        tple[i] = sum(set(j))

def generate_files(filesnames,s):
    '''
    
    
    Write a function that, given a list of filenames (strings) and a directory (string)...
creates the directory, if it does not already exist
generates one file for each of the given filenames
The contents of each file is the name of the file (e.g., if one of the filenames is hello.txt the file would contain just hello)

A note to be careful of -- if the directory already exists, and you create files with the given names, they’ll overwrite any existing files that already have those names. Just make sure you’re testing your function with brand-new directory names that you don’t already have!

Here are the specs:
Function name: generate_files
Parameters: list of strings (filenames), directory name (string)
Returns: nothing (when we test your function, we’ll use the OS library to verify that the files exist in the correct directory)

Examples of calling your function:
generate_files(["hello.txt", "bye.txt"], "mydir") ..... returns nothing but creates the file mydir/hello.txt and the file mydir/bye.txt. The first file contains the text “hello”, and the second file contains the text “bye”.
'''
    if not os.path.exists(s):
        os.makedirs(s)
    
    
    for filename in filesnames:
        file_path = os.path.join(s, filename)
        with open(file_path, 'w') as file:
            file_content = os.path.splitext(filename)[0]
            file.write(file_content)




def combine_dcts(twodlst_lists):
    '''
    Write a function that, given a list 2D lists, creates a dictionary where every header element becomes a key and the corresponding column becomes its value, as a list. This should sound just like lab2! However, now we’ll have multiple 2d lists! For each new list, tack it on to the existing dictionary. If one of its header elements already exists as a key in the dictionary, overwrite it with the new value.
 
Imagine two different 2d lists representing a CSV files with a header, like this:
name
attribute 
fault
Grizz
happy 
barking
Carol
hugs
jealous


name
age 
GRIZZ!!!!
2 
Carol
2


We want it to turn into a single dictionary where the keys come from the header, and the values are lists. Both the 2d lists end up in the same dictionary.
{"name" : ["GRIZZ!!!", "Carol"],
 "attribute" : ["happy", "hugs"],
 "fault" : ["barking", "jumping"],
 "age" : [2, 2]}

Here are the specs:
Function name: combine_dcts
Parameters: list of 2d lists
Returns: dictionary 

Example of calling your function:
combine_dcts([ [["h1", "h2"], [1, 2], [3, 4]],
   [["h2", "h3"], [5, 5], [6, 6]] ]) .....
 returns {"h1" : [1, 3], "h2" : [5, 6], "h3" : [5, 6]} 

    
    '''
    
    
    combined_dct = {}
   
    for lst in twodlst_lists:
        headers = lst[0]
        for i, header in enumerate(headers):
            if header in combined_dct and lst is not twodlst_lists[0]:
               combined_dct[header] = [row[i] for row in lst[1:]]
            elif header not in combined_dct:
                
                combined_dct[header] = [row[i] for row in lst[1:]]
            else:
               
                combined_dct[header].extend([row[i] for row in lst[1:]])
    return combined_dct



    
    
    