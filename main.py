"""
Sadia Plimley
CIS-30A Summer 2025
Final Project: Keylogger
Program Purpose: To monitor all user inputs on their device
and track them in a file. Additionally, organize the data to show statistics
on the user's inputs
 ----- main file
"""

import threading
import keylog_control
import keylog_mouse
from pynput import keyboard, mouse

# Start keyboard listener
def start_keyboard():
    with keyboard.Listener(on_press=keylog_control.writeToLog) as listener:
        listener.join()

# Start mouse listener
def start_mouse():
    with mouse.Listener(on_move=keylog_mouse.writetomog) as listener:
        listener.join()

# Start both listeners in parallel
threading.Thread(target=start_keyboard, daemon=True).start()
threading.Thread(target=start_mouse, daemon=True).start()

# Display welcome message
print("Welcome to the Keylogger 3000! We have designed a state of the art")
print("keylogger for your enjoyment and education! It's important to note that")
print("The keylogger is already on! It was that easy. As long as this program is")
print("running, we will be monitoring your device and tracking everything you type/do")
print("In the meantime, explore the web! Text your friends! Our program")
print("will be here waiting and you can see our logs whenever you want.")

# Define command functionality
class Run:
    def display(self, log):
        print(f"\n--- Displaying {log} ---")
        try:
            with open(log, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print(f"{log} not found.")

    def clear_logs(self):
        with open("log.txt", 'w'), open("mog.txt", 'w'): # put in w mode to clear all text
            pass
        print("Your logs have been cleared!")

    def mouse_tp(self):
        keylog_control.ctrl_mouse()# moves mouse to random location
        keylog_control.ctrl_keyboard() #types a word on keyboard
        print("Mouse and keyboard teleportation executed.")

# Command menu
commands = {
    "A": "Display Keyboard Log",
    "B": "Clear Logs",
    "C": "Display Mouse Log",
    "D": "Mouse Teleportation",
    "E": "Kill Program"
}

print("\nCommand Menu:")
for k, v in commands.items(): #prints out all commands for user
    print(f"{k}: {v}")

# Command loop
run = Run()
while True:
    choice = input("\nWhich command would you like to run? ").strip().upper() #make uppercase
    if choice == "A": #if a, run display function
        run.display("log.txt")
    elif choice == "B": #if b, run clear log
        run.clear_logs()
    elif choice == "C": #if c, run display mog
        run.display("mog.txt")
    elif choice == "D":
        run.mouse_tp() #if d, run mouse teleportation
    elif choice == "E":
        print("Exiting program...")
        break #end program 
    else:
        print("Invalid input. Please choose A, B, C, D, or E.")



""" Sadia Ideas:

2 classes, 1 subclass ( ) used for characters, subclass for letters bc we need to add A & a
together to have combined letter count. 2nd class is for IDK YET maybe the commands?
 --- class must have 1 object ( )count for how many times pressed & 1 method ( ) counting
list  (X) of all characters that shows how many times you've written them
strings (X) used to talk to user in console + for actual keylogging lol
2+ functions (X) for displaying and logging
while or for loop (X) for display of character usage (see character usage? yes. show all)
conditional statement (X) for cleaning key data
custom module (X) control module and mouse module
error detection. ruh roh (X) for user input of commands
file operations and output (X) log.txt
NO UI >:(


Program runs as follows :

- turn on keylogger + keycounter 
- say hi to user, explain everything, tell them to do stuff w their laptop
- give list* of commands (display log.txt, see stats, clear log.txt, display mog.txt,
kill program), get input response & use error detection there

"""

