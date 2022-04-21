# GForce_2

Gforce_2

Created by: Michael J Evan ATP, CFII                                                           

In addition to Software Engineering I am also a Commercial Pilot / ATP (Airline Transport Pilot) Multi-Engine Rated and
Certified Flight & Instrument Instructor & Ground Instructor. This program is only intended to be used for theoretical representation of Bank Angle and how it effects Load Factor and Stall Speed. It should never be used for actual aircraft specific pre-flight performance calculations and such use is prohibited
by this disclaimer.

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user selects for the aircraft. The initial stall speed selected should be for the aircraft at 1G in level flight.

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via the 2 dials in the center of the user interface with a mouse or laptops trackpad.

GForce_2: This program was coded utilizing the python programming language. It performs all the aerodynamic calculations and interacts with gForc_2_UI.py program to display all of its calculations on the GUI (graphical user interface). Qt_designer was utilized to layout the GUI. Qt_designer then generates a .ui file in HTML format which then must be converted to a python program. The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to accomplish this conversion. That program creates the actual GUI that the user interacts with. If you would like to replicate this process download the GForce_2.py & the GForce_2_Ui.ui files and load into your favorate python editor/ide. Enter the following command via the terminal in the editor:

pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

Then run GForce_2.py from the editor/ide.

You will obviously need to install pyqt6 in order to compile the .ui file to a python .py program which allows the Graphical user interface to be generated. You don't need to download the gForce_2_UI.py file if you choose to experiment using the pyuic6 command in the terminal since this file will be generated with the pyuic6 command. You only need the .ui file.  You can call the .py user interface file whatever you want but changing the name will cause a need for a slight refactoring of code in the main python program. The UI_MainWindow is imported from the user interface Python file.

If you change the name of the file the line shown below which sits near the beginning of the main Python program needs to be changed:

from gForce_2_UI import Ui_MainWindow   

This line near the top of the main .py program would need to be changed by inserting the file name that you used right after the word from. 
If your using Visual Studio Code it will ask to refactor the program which will do this for you. Other IDE's will possible do the same but if not, the program name won't be corrected and an error would be generated if the file names don't match.

The program will need a current version of Python3 on your system to run the above code.........python 3.8.9 was utilized during the development of this software. Mac computers should already have a version of Python3 pre installed. If your not familiar with programming I would just download the .dmg file and enjoy the program. 

The GForce_2_Installer.dmg file is your typical Apple Mac instalation package file. Download the file to your Mac. Double click the .dmg and drag the
icon to the applications folder. Double clicking the program icon will then lauch the program interface. To exit the program click the red dot in the upper left corner of the GUI. ENJOY..... It's FREE!!!!!


Below is a screen shot of the program:

![GForce_2 ScreenShot](https://user-images.githubusercontent.com/49410936/163623163-b7338b71-79a0-46a7-a7da-ced7d99bc936.png)
