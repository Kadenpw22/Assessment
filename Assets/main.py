"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

print("--------------------------")
print("Disneyland Review Analyser")
print("--------------------------")

import process
import tui
import visual
import csv


def view(data):
    parks = process.park_names(data)
    while True:
        choice = tui.view_data_menu()
        if choice == "A":
            tui.park_choice(parks)
            rows = process.choose_name(data, park)
            tui.display_rows(rows, limit = 50)
# def run():
#     park_data = process.load_dataset("disneyland_reviews.csv")
#     while True:
#         choice = tui.main_menu()
#         if choice == "A":



