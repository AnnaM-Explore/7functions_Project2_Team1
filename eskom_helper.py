import numpy as np
import pandas as pd

def dictionary_of_metrics(items):

    arr = np.array(items)

    #create a dictionary
    my_dict = {'mean': round(arr.mean(),2),
                'median': round(np.median(items),2),
                'variance': round(np.var(items),2),
                'standard deviation': round(np.std(items),2),
                'min': round(arr.min(),2),
                'max': round(arr.max(),2)}
    
    return my_dict