"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import process
import tui
import visual
import csv

print("--------------------------")
print("Disneyland Review Analyser")
print("--------------------------")

def display_view_data_menu(data):
    while True:
        option = tui.view_data_menu()
        if option == "A":
            break
        elif option == "B":
            break
        elif option == "C":
            break
        elif option == "D":
            break
        elif option == "X":
            return
        else:
            print("Invalid option")
def display_visualise_menu(data):
    while True:
        option = tui.visualise_menu()
        if option == "A":
            break
        elif option == "B":
            break
        elif option == "C":
            break
        elif option == "X":
            return
        else:
            print("Invalid option")
def run():
    data = process.load_dataset("disneyland_reviews.csv")
    tui.display_dataset(len(data))
    while True:
        option = tui.main_menu()
        if option == "A":
            display_view_data_menu(data)
        elif option == "B":
            display_visualise_menu(data)
        elif option == "X":
            print("Goodbye!")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    run()







