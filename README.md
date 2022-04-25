# GForce_2

Gforce_2

There are 3 different installation files in the above files listing. One for Intel based Macs, M1 Mac, & Windows:

Installer for Intel Macs: GF2IntelMac.dmg

Installer for M1 Macs: GForce2_M1Mac.dmg

Installer for Windows: GForce_2_Windows_Installer.exe

Created by: Michael J Evan ATP, CFII                                                           

In addition to Software Engineering I am also a Commercial Pilot / ATP (Airline Transport Pilot) Multi-Engine Rated and
Certified Flight & Instrument Instructor & Ground Instructor, and Nurse Anesthetist. This program is only intended to be used for theoretical representation of Bank Angle and how it effects Load Factor and Stall Speed. It should never be used for actual aircraft specific pre-flight performance calculations and such use is prohibited
by this disclaimer.

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user selects for the aircraft. The initial stall speed selected should be for the aircraft at 1G in level flight.

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via the 2 dials in the center of the user interface with a mouse or laptops trackpad.  Calculations are done in real time via function calls with each click of any dial.

GForce_2: This program was coded utilizing the python programming language. It performs all the aerodynamic calculations and interacts with gForc_2_UI.py program to display all of its calculations on the GUI (graphical user interface). Qt_designer was utilized to layout the GUI. Qt_designer then generates a .ui file in HTML format which then must be converted to a python program. The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to accomplish this conversion. That program creates the actual GUI that the user interacts with. If you would like to replicate this process download the GForce_2.py & the GForce_2_Ui.ui files and load into your favorate python editor/ide. Enter the following command via the terminal in the editor:

pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

Then run GForce_2.py from the editor/ide.  The program should display as shown below.

You will need to install pyqt6 in order to compile the .ui file to a python .py program which allows the Graphical user interface to be generated. You don't need to download the gForce_2_UI.py file if you choose to experiment using the pyuic6 command in the terminal since this file will be generated with the pyuic6 command. You only need the .ui file.

None programmers please just use one of the 3 installation files provided depending on your operating system. Currently there is no Linux distribution. But ya never know!

Below is a screen shot of the program:

![GForce_2 ScreenShot](https://user-images.githubusercontent.com/49410936/163623163-b7338b71-79a0-46a7-a7da-ced7d99bc936.png)
