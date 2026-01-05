"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import tui
import csv

with open("disneyland_reviews.csv", newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)
row_count = len(rows)
print("Number of rows: ", row_count)

def get_unique_parks(data):
    return sorted({row["Branch"] for row in data})
def filter_by_park(data, park):
    return [row for row in data if row["Branch"] == park]
