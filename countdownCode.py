import time # Import the time module. This module is already in the pip package, no reason to pip install

''' Provide function docstring by using a multiline comment. 
These are typically only used when you are describing the use of a function. It does not have to be a long
drawn out book, but you should be able to briefly explain the purpose and function of the program to anyone
Who is not familiar with coding. Clear enough for them to have the ability and be like 'oooh, That is what it does.'
Make sure that you use 3 single quotations to make a multiline comment or docString '''

def timerCountdown(userTime): # define a function that uses the parameter of the variable of the input
    while userTime: # start the while loop
        min, secs = divmod(userTime, 60) # divmode function used for two variables. min and second by using
        # The user input and dividing it by 60
        timer = '{:02d}:{:02d}'.format(min, secs) # Once we identify the min and seconds through divmod, we can use them
        # To set our timer accordingly in a proper format
        print('\r', timer, end='') # Prints the timer using carriage returns
        # What is a carriage return?
        time.sleep(1) # uses the sleep function from the time library to create a one-second delay
        userTime -= 1 # Takes the userTime and subtract one from the total for each second
    # While loop ends
    print('\n Timer Completed') # prints on a new line timer completed, once the timer runs out of the seconds provided+


userTime = input('Please enter the time in seconds: \n') # creates the input variable to get the user time in seconds
# userTime as a parameter to run the function

timerCountdown(int(userTime)) # calls the timer countdown function
# converts the userTime string into an integer and then pushes it through the parameter.


# Extra Practice:
# 1) Use Audio library:
# Countdowns typically have timers, or a loud noise to alert the user that the timer has reached the end.
# You will want to import a new library to add audio to your timer.
# There are three libraries you can choose from: playsound, tkinter snack sound, & native player

# 2) Expand the program with a date countdown as well
# Create a menu to allow the user to set a timer or a date countdown.
# Allow the user to see the date countdown as well (similar aspect to the timer)
# You will need to import dateTime library - read the documentation provided by Ms. Adami
# When the program asks for the date, have it also ask to name the date count down.

# 3) Expand even more:
# allow the user to set multiple timers. Once a timer is set, allow the user to add a description or name it
# Allow the user to know what timer belongs to what.
# All the timers should still be able to run as the program is running, if the program closes, so will the alarms

# 4) If you want to go crazy: Make a gui inteface
# It is understandable that you have absolutely no clue how to use Tkinter, but if you want to try to make a GUI
# interface
# You can import the library - tkinter
# Use the documentation provided by Ms. Adami as an aid. We haven't learned tKinter, so I do not expect you to make it
# perfect, but if you want to give it a shot, please feel free too
# Design the user interface how you would like. When we do this assignment again, when we do tKinter, I will show
# a specific
# way since the class will be doing it together. However, if you want to attempt this, please feel free to design it
# As you want
