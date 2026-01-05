"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
from collections import defaultdict

import tui
import csv

def park_names(data):
    parks = []
    for row in data:
        park = row["Column"]
        if park not in parks:
            parks.append(park)
    parks.sort()
    return parks
def choose_name(data, park):
    row_sort = []
    for row in data:
        if row["Column"] == park:
            row_sort.append(row)



