'''
Write the following function:
* name: filter_line
* parameters: string, list, list
* returns: filtered/smaller version of second list

  Given...
    - the name of an MBTA line (green, orange, red, etc.)
    - a list of MBTA lines (green line, orange line, etc.)
    - a second list that corresponds with the first (same size)
    
   Return...
    - a filtered version of the second list.
      
   For example, given:
         "green", ["green line", "red line", "green line"], [3, 4, 5]
         
    Your function should return a filtered version of the second list, 
    wherever "green" was found in the first:
        [3, 5]
        
    Because the file we're working with uses different names for the lines,
    your function should be able to take in "green" or "Green" and find the
    corresponding value "green line" or "Green Line" or "GREEN LINE"


'''


def filter_line(s, lst,lst2):
    #find the instances in the first list where the value of s corresponds to the line in lst.
    #then uses the second list parameter to figure out the corresponding numbers to print out
    s_lower = s.lower()
    #creating a new lst to store the sorted values of the second lst. 
    newlst=[]
    #zipping together the corresponding line with the value
    for x,z in zip(lst,lst2):
        

        #making sure that the value of what line is in the zipped up lsts. 
        if s_lower in x.lower():
            #adding the value corresponding to the correct line to the new lst
            newlst.append(z)
    #returning the new list
    return newlst

