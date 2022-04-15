

"""
This program uses the aerodynamics formulas:

1/cos(bank_angle) = load factor for an aircraft in a level turn for a selected angle of bank

New Stall speed = Stall Speed in level flight * Sqrt(g_force)

Note: the calculation for stall speed is based on entering the speed in knots

Numeric input by the user is selected by rotating 2 dials, left dial for stall speed in level flight
and right dial for selecting the desired angle of bank.


"""
# note: must convert to radians when using trig functions in python

import sys
import math

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from gForce_2_UI import Ui_MainWindow  # from the new python class file we created "Ui_gForce" in the terminal; import Ui_MainWindow

bank_angle = int(0)  # initializes the bank angle to an integer value
stall_speed = int(40) # initialized stall speed to integer with minimum value of 40 knots
stall_speed_banked = int(40) # stall speed displayed at the selected angle of bank....initialized at 40 i.e. 1g or level flight
g_force = float(0.0)   # initializes the G force to a float




class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.bankangledial.valueChanged.connect(self.dial_rotated)
        self.ui.StallSpeedDial.valueChanged.connect(self.dial_rotated)
        
    def show(self):    # displays main window
        self.main_win.show()

    # connect signals to appropriate slots

    def dial_rotated(self):     # outputs the bank angle on the main page when the dial is rotated
        global bank_angle       # global for use in load factor calculation function
        global stall_speed   #global to calculate new stall speed
        bank_angle = int(self.ui.bankangledial.value())
        stall_speed = int(self.ui.StallSpeedDial.value())
        self.ui.bankanglevalue.setNum(bank_angle)
        self.ui.bankanglevalue_2.setNum(bank_angle)
        self.ui.stallspeedvalue.setNum(stall_speed)
        self.g_force_stall_calc()
        self.g_force = str(g_force)   # new code to convert the g force output to str to be formatted 2 decimal place
        self.stall_speed_banked = str(stall_speed_banked) #stall speed banked converts to string for output
        self.ui.gForce_value.setText("{:0.2f}".format(g_force)) # formats all output as a str with 2 dec place
        self.ui.newstallspeedvalue.setText(format(stall_speed_banked)) # formats sting output of new stall speed.

#   aerodynamics function that calculates the load facter based on an aircraft angle of bank in a level turn.
#   g_Force variable is made global to enable its output to be displayed by another function

    def g_force_stall_calc(self):   # calculates the load factor from users chosen angle of bank
        global g_force
        global stall_speed_banked
        cos_bank_angle = math.cos(math.radians(bank_angle))
        g_force = 1 / cos_bank_angle
        stall_speed_banked = int(stall_speed * math.sqrt(g_force))


# below is boilerplate for every program for the main window, other ui components don't need it.
# I'll use this only for the entry main window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
