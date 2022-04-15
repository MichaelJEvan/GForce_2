# GForce_2

Gforce_2

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user "dials in" for the aircraft. The stall speed selected should be for the aircraft at 1G in level flight.......

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via 2 dials so there is no chance of invalid data input by the user

This is a python3 program that also utilizes Qt_designer to layout the GUI (graphical user interface)......... It generates a .ui file in HTML format

The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to convert it to a python program.

Enter the following command in the terminal to convert: pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

You will need to install pyqt6 in order to compile the .ui file to a python file to allow the Graphical user interface to be generated.... Obviously this can all be done from the terminal in your favorite IDE/Editor. You don't need to download the gForce_2_UI.py file since this is generated with the pyuic6 command entered in the terminal shown above. You can call this file whatever you want but a refactoring will need to be done in your main python program.
If you change the name of the file this line at the beginning of the main Python program needs to be changed:

from gForce_2_UI import Ui_MainWindow   <------ this line at the top of the main .py program would need to be changed by inserting the file name that you used right after the from.  If your using Visual Studio Code it should ask to refactor the program which would do this for you.

This program should work with a current version of Python3.........I utilized python 3.8.9

I will have a .dmg file available shortly for anyone that would like to utilize the program on a Mac computer. Enjoy!

Below is a screen shot of the program:

![GForce_2 ScreenShot](https://user-images.githubusercontent.com/49410936/163623163-b7338b71-79a0-46a7-a7da-ced7d99bc936.png)
