"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
while True:
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    choice = input("Please enter the letter that corresponds with your desired menu choice")
    if choice == "A":
        print("You have chosen option A - View Data")
        print("[A] View Reviews by Park")
        print("[B] Number of Reviews by Park and Reviewer location")
        print("[C] Average score per year by park")
        print("[D] Average score per park by reviewer location")
        print("Please enter one of the options")
    elif choice == "B":
        print("You have chosen option B - Visualise Data")
        print("[A] Most reviewed parks")
        print("[B] Park rank by nationality")
        print("[C] Most popular month by park")
    elif choice == "X":
        print("You have chosen option X - Exit")
        break
    else:
        print("That is an invalid menu choice. Try again.")
