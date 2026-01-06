"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
from collections import defaultdict

import tui
import csv

def load_dataset(file_path):
    data = []
    with open("disneyland_reviews.csv", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

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
def reviews_count(data, park, location):
    count = 0
    for row in data:
        if row["Column"] == park and row["Review_Location"] == location:
            count += 1
    return count



