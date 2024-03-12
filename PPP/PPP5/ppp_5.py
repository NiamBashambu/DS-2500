'''
Filename: ppp_5.py

Write the following function:
* name: find_majority_class
* parameters: list of classes (strings), list of tuples [(x, y, z),
  (x, y, z), ..., (x, y, z)].
  One of the values in each tuple is a class, but we 
  don’t know which one.
* returns: a string, the most common class found in the tuple

For example...
Given ["cat", "dog"], [("cat", 3, 4)], your function should return "cat"
Given ["cat", "dog"], [("cat", 3, 4), ("cat", 5, 6), (5, 6, "dog"), (4, "cat", 18), (15, -1, "dog")], your function should return "cat"
Given ["x", "y"], [(3, 4, "y"), (5, "y", 6), (5, 6, "y"), (4, "x", 18)], your function should return "y"
Given ["x", "y", "z"], [(3, 4, "y"), (5, "z", 6), (5, 6, "x"), (4, "x", 18)], your function should return "x"

You can assume that exactly one of the elements in each tuple is the name of one of the classes, and it’s an exact match. You can also assume that there are no ties.


'''

def find_majority_class(class_str,tuple_list):
    class_counts = {}
    for class_name in class_str:
        class_counts[class_name] = 0
    
    
    for current_tuple in tuple_list:
        for class_name in class_str:
            if class_name in current_tuple:
                class_counts[class_name] += 1
                break  
    
    majority_class = max(class_counts, key=class_counts.get)
    
    return majority_class