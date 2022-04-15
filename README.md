# GForce_2

Gforce_2
Created by: Michael J Evan.........................
In addition to Software Engineering as a hobby I'm also a Commercial Pilot with ATP (Airline Transport Pilot) Multi-Engine Rating and a
Certified Flight/Instrument/Ground Instructor.

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user "dials in" for the aircraft. The stall speed selected should be for the aircraft at 1G in level flight.......

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via 2 dials so there is no chance of invalid data input by the user

This is a python3 program that also utilizes Qt_designer to layout the GUI (graphical user interface)......... It generates a .ui file in HTML format

The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to convert it to a python program.

Enter the following command in the terminal: pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

You will need to install pyqt6 in order to compile the .ui file to a python file to allow the Graphical user interface to be generated.... Obviously this can all be done from the terminal in your favorite IDE/Editor. You don't need to download the gForce_2_UI.py file if you choose to experiment using the pyuic6 command in the terminal since this file will be generated with the pyuic6 command. You only need the .ui file.  You can call the .py user interface file whatever you want but changing the name will cause a need for a slight refactoring of code in the main python program. The UI_MainWindow is imported from the user interface Python file.

If you change the name of the file the line near the beginning of the main Python program needs to be changed:

from gForce_2_UI import Ui_MainWindow   

This line near the top of the main .py program would need to be changed by inserting the file name that you used right after the word from. 
If your using Visual Studio Code it should ask to refactor the program which would do this for you. Other IDE's will possible do the same since an error would be generated if the file names don't match.

The program should work with a current version of Python3.........I utilized python 3.8.9

I will have a .dmg file available shortly for anyone that would like to utilize the program on a Mac computer. Enjoy!

Below is a screen shot of the program:

![GForce_2 ScreenShot](https://user-images.githubusercontent.com/49410936/163623163-b7338b71-79a0-46a7-a7da-ced7d99bc936.png)
