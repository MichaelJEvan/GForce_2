# GForce_2

Gforce_2

3 different installation files are located in the list above:  Intel Mac, M1 Mac, & Windows

Installer file Intel Mac: GF2IntelMac.dmg

Installer file M1 Mac: GForce_2_M1Mac.dmg

Installer file Windows 7 thru 10, possibly Windows 11: GForce_2_Windows_Installer.exe

Created by: Michael J Evan ATP, CFII                                                           

In addition to Software Development, I am also a Commercial Pilot / ATP (Airline Transport Pilot) Multi-Engine Rated and
Certified Flight & Instrument Instructor & Ground Instructor, and Nurse Anesthetist. This program is only intended to be used for theoretical representation of Bank Angle and how it effects Load Factor and Stall Speed. It should never be used for actual aircraft specific pre-flight performance calculations and such use is prohibited
by this disclaimer.

The program calculates G-force/Load Factor on an airplane at a constant altitude and a constant angle of bank. It will also calculate the new stall speed for the selected angle of bank based on what stall speed the user selects for the aircraft. The initial stall speed selected should be for the aircraft at 1G in level flight.

There is no user input via the keyboard......... Stall Speed & Angle of Bank are both selected via the 2 dials in the center of the user interface with a mouse or laptops trackpad.  Calculations are done in real time via function calls with each click of any dial.

GForce_2: This program was coded utilizing the python programming language, Version 3.8. It performs all the aerodynamic calculations and interacts with gForc_2_UI.py program to display all of its calculations on the GUI (graphical user interface). Qt_designer was utilized to layout the GUI. Qt_designer then generates a .ui file which then must be converted to a python program. The gForce_2_UI.py is creating using pyqt6 via command line on the .ui to accomplish this conversion. That program creates the actual GUI that the user interacts with. If you would like to replicate this process download the GForce_2.py & the GForce_2_Ui.ui files, load into your favorate python editor/ide and have a blast! You will need pyqt6 installed on your Mac and older macs will require pyqt5 with the need to refactor your code in the GForce_2.py to change the imports to pyqt5.  

Entering the following command via the terminal in the editor will do the conversion of the .ui file to a .py file:

pyuic6 -x GForce_2_UI.ui -o gForce_2_UI.py

Run GForce_2.py from the terminal in your editor/ide with the command below:

python3 GForce_2.py

The program should display as shown below.

You will need to install pyqt6 in order to compile the .ui file to a python .py program which allows the Graphical user interface to be generated. You don't need to download the gForce_2_UI.py file if you choose to experiment using the pyuic6 command in the terminal since this file will be generated with the pyuic6 command. You only need the .ui file.

None programmers please just use one of the 3 installation files provided depending on your operating system. Currently there is no Linux distribution. But ya never know!

Below is a screen shot of the program with example values selected:

![GForce_2 Screenshot](https://user-images.githubusercontent.com/49410936/165987633-46618654-ad2a-499e-8179-9ac31cacb54b.png)

