""" Sadia Plimley
CIS-30A Summer 2025
Final Project: Keylogger
Program Purpose: To monitor all user inputs on their device
and track them in a file. Additionally, organize the data to show statistics
on the user's inputs """

# ///// MOUSE FILE /////
# purpose: to listen to mouse and see its positions

from pynput.mouse import Listener

def writetomog(x,y):
    with open("mog.txt", "a") as mog: #create mouse log
        mog.write("Position of current mouse: {0}".format((x,y)))
        #append mouse position to mog

with Listener(on_move=writetomog) as listener:
    listener.join()
