# Form implementation generated from reading ui file 'g_force_tester_2.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1115, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 232, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 31))
        self.label_2.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.bankanglevalue = QtWidgets.QLabel(self.centralwidget)
        self.bankanglevalue.setMinimumSize(QtCore.QSize(50, 31))
        self.bankanglevalue.setMaximumSize(QtCore.QSize(50, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.bankanglevalue.setFont(font)
        self.bankanglevalue.setAutoFillBackground(False)
        self.bankanglevalue.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bankanglevalue.setIndent(5)
        self.bankanglevalue.setObjectName("bankanglevalue")
        self.horizontalLayout_2.addWidget(self.bankanglevalue)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(258, 31))
        self.label.setMaximumSize(QtCore.QSize(258, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setToolTipDuration(-1)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gForce_value = QtWidgets.QLabel(self.centralwidget)
        self.gForce_value.setMinimumSize(QtCore.QSize(85, 31))
        self.gForce_value.setMaximumSize(QtCore.QSize(85, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.gForce_value.setFont(font)
        self.gForce_value.setIndent(5)
        self.gForce_value.setObjectName("gForce_value")
        self.horizontalLayout_2.addWidget(self.gForce_value)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.bankanglestalllabel = QtWidgets.QLabel(self.centralwidget)
        self.bankanglestalllabel.setEnabled(True)
        self.bankanglestalllabel.setMinimumSize(QtCore.QSize(135, 30))
        self.bankanglestalllabel.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setKerning(True)
        self.bankanglestalllabel.setFont(font)
        self.bankanglestalllabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bankanglestalllabel.setAutoFillBackground(False)
        self.bankanglestalllabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bankanglestalllabel.setIndent(0)
        self.bankanglestalllabel.setObjectName("bankanglestalllabel")
        self.horizontalLayout_2.addWidget(self.bankanglestalllabel)
        self.newstallspeedvalue = QtWidgets.QLabel(self.centralwidget)
        self.newstallspeedvalue.setMinimumSize(QtCore.QSize(80, 0))
        self.newstallspeedvalue.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.newstallspeedvalue.setFont(font)
        self.newstallspeedvalue.setObjectName("newstallspeedvalue")
        self.horizontalLayout_2.addWidget(self.newstallspeedvalue)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.instruction_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.instruction_label.setFont(font)
        self.instruction_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.instruction_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.instruction_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.instruction_label.setObjectName("instruction_label")
        self.horizontalLayout.addWidget(self.instruction_label)
        spacerItem5 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.StallSpeedTextLable = QtWidgets.QLabel(self.centralwidget)
        self.StallSpeedTextLable.setMinimumSize(QtCore.QSize(225, 30))
        self.StallSpeedTextLable.setMaximumSize(QtCore.QSize(225, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.StallSpeedTextLable.setFont(font)
        self.StallSpeedTextLable.setObjectName("StallSpeedTextLable")
        self.horizontalLayout_6.addWidget(self.StallSpeedTextLable)
        self.stallspeedvalue = QtWidgets.QLabel(self.centralwidget)
        self.stallspeedvalue.setMinimumSize(QtCore.QSize(50, 0))
        self.stallspeedvalue.setMaximumSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stallspeedvalue.setFont(font)
        self.stallspeedvalue.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stallspeedvalue.setObjectName("stallspeedvalue")
        self.horizontalLayout_6.addWidget(self.stallspeedvalue)
        self.StallSpeedDial = QtWidgets.QDial(self.centralwidget)
        self.StallSpeedDial.setMinimumSize(QtCore.QSize(100, 150))
        self.StallSpeedDial.setMaximumSize(QtCore.QSize(200, 16777215))
        self.StallSpeedDial.setMinimum(40)
        self.StallSpeedDial.setMaximum(150)
        self.StallSpeedDial.setProperty("value", 40)
        self.StallSpeedDial.setWrapping(False)
        self.StallSpeedDial.setNotchTarget(0.699999999999999)
        self.StallSpeedDial.setNotchesVisible(True)
        self.StallSpeedDial.setObjectName("StallSpeedDial")
        self.horizontalLayout_6.addWidget(self.StallSpeedDial)
        self.bankangledial = QtWidgets.QDial(self.centralwidget)
        self.bankangledial.setMinimumSize(QtCore.QSize(200, 261))
        self.bankangledial.setMaximumSize(QtCore.QSize(200, 260))
        self.bankangledial.setMaximum(89)
        self.bankangledial.setNotchTarget(2.7)
        self.bankangledial.setNotchesVisible(True)
        self.bankangledial.setObjectName("bankangledial")
        self.horizontalLayout_6.addWidget(self.bankangledial)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.bankanglevalue_2 = QtWidgets.QLabel(self.centralwidget)
        self.bankanglevalue_2.setMinimumSize(QtCore.QSize(30, 0))
        self.bankanglevalue_2.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bankanglevalue_2.setFont(font)
        self.bankanglevalue_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bankanglevalue_2.setIndent(5)
        self.bankanglevalue_2.setObjectName("bankanglevalue_2")
        self.horizontalLayout_6.addWidget(self.bankanglevalue_2)
        self.bankanglelabel = QtWidgets.QLabel(self.centralwidget)
        self.bankanglelabel.setMinimumSize(QtCore.QSize(0, 30))
        self.bankanglelabel.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.bankanglelabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.bankanglelabel.setFont(font)
        self.bankanglelabel.setObjectName("bankanglelabel")
        self.horizontalLayout_6.addWidget(self.bankanglelabel)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "  GForce_2   -   Programmed by: Michael J. Evan ATP-CFII   -   Version 1.0.0   © 2022 "))
        self.label_2.setText(_translate("MainWindow", "Degree Angle of Bank :"))
        self.bankanglevalue.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "   ="))
        self.label.setText(_translate("MainWindow", "Load Factor / G-Force :"))
        self.gForce_value.setText(_translate("MainWindow", "1.0"))
        self.label_4.setText(_translate("MainWindow", "= "))
        self.bankanglestalllabel.setText(_translate("MainWindow", "Stall Speed :"))
        self.newstallspeedvalue.setText(_translate("MainWindow", "40"))
        self.instruction_label.setText(_translate("MainWindow", "Select Stall Speed in knots of aircraft in level flight and Angle of Bank"))
        self.StallSpeedTextLable.setText(_translate("MainWindow", "Stall Speed Level Flight:"))
        self.stallspeedvalue.setText(_translate("MainWindow", "40"))
        self.bankanglevalue_2.setText(_translate("MainWindow", "0"))
        self.bankanglelabel.setText(_translate("MainWindow", "Degree Angle of Bank"))
        self.label_5.setText(_translate("MainWindow", "Disclaimer: The following program was designed to show the pilot the aerodynamic relationships between bank angle and it\'s effects on Load Factor & Stall Speed in a level constant speed turn. It should not be utilized for actual aircraft flight performance calculations and should only be used as a theoretical teaching tool for demonstrating the above relationships."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
