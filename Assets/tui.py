"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import process
def main_menu():
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    choice = input("Enter the letter that corresponds with your desired menu choice: ")
    print(f"You entered: {choice}")
    return choice
def view_data_menu():
    print("[A] View Reviews by park")
    print("[B] Number of reviews by park and reviewer location")
    print("[C] Average score per year by park")
    print("[D] Average score per park by reviewer location")
    choice = input("Enter the letter that corresponds with your desired menu choice: ")
    print(f"You entered: {choice}")
    return choice
def visualise_menu():
    print("[A] Most reviewed parks")
    print("[B] Park ranking by nationality")
    print("[C] Most popular month by park")
    choice = input("Enter the letter that corresponds with your desired menu choice: ")
    print(f"You entered: {choice}")
    return choice