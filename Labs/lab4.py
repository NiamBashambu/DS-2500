import statistics


def normalize(lst):
    '''
    given a list of numbers, return a list of min/max normalized values
    
    '''
    minn = min(lst)
    maxx = max(lst)

    normal = []

    for x in lst:
        normal_x = (x-minn)/((maxx-minn))
        normal.append(normal_x)
    return normal


def z_score(lst):
    newlst = []
    mean = sum(lst)/len(lst)
    stdevv = statistics.stdev(lst)
    for i in lst:
        num = i-mean
        newval = num/stdevv
        newlst.append(newval)
    return newlst

def hamming(s,s2):

    i =0
    for s,s2 in zip(s,s2):
        if s!=s2:
            i+=1
    return i





        
