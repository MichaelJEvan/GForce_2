# GForce_2


![GForce_2 Screenshot](https://user-images.githubusercontent.com/49410936/165987633-46618654-ad2a-499e-8179-9ac31cacb54b.png)


Downloadable installation file is located in the files list of this repository for the following platforms: M1 Mac, & Windows.

Installer file Windows 7 thru 10, Windows 11 has not been tested yet: GForce_2_Windows_Installer.exe

NOTE: Compiling and conversion instructions below are for programmers only that wish to tinker. You don't need to do any of that to install.

Created by: Michael J Evan ATP, CFII                                                           

This program is only intended to be used for theoretical representation of Bank Angle and how it effects Load Factor and Stall Speed. It should never be used for actual aircraft specific pre-flight performance calculations and such use is prohibited
by this disclaimer.

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user selects for the aircraft. The initial stall speed selected should be for the aircraft at 1G in level flight.

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via the 2 dials in the center of the user interface with a mouse or laptops trackpad.  Calculations are done in real-time via function calls with the movement of any dial.

GForce_2: This program was coded utilizing the python programming language, Version 3.8. It performs all the aerodynamic calculations and interacts with gForc_2_UI.py program to display all of its calculations on the GUI (graphical user interface). Qt_designer was utilized to layout the GUI. Qt_designer then generates a .ui file which then must be converted to a python program. The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to accomplish this conversion. That program creates the actual GUI that the user interacts with. If you would like to replicate this process download the GForce_2.py & the GForce_2_Ui.ui files, load into your favorate python editor/ide and have a blast! You will need pyqt6 installed on your Mac or Windows platform and older hardware may require pyqt5 with the need to refactor your code in the GForce_2.py program to change the imports to pyqt5.

Entering the following command via the terminal in the editor will do the conversion of the .ui file to a .py file:

pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

Run GForce_2.py from the terminal in your editor/ide with the command below:

python3 GForce_2.py

The program should display as shown below.

You will need to install pyqt6 in order to compile the .ui file to a python .py program which allows the Graphical user interface to be generated. You don't need to download the gForce_2_UI.py file if you choose to experiment using the pyuic6 command in the terminal since this file will be generated with the pyuic6 command. You only need the .ui file.

Non programmers please just use one of the 3 installation files provided depending on your operating system and enjoy the program. Currently there is no Linux distribution. But ya never know!




