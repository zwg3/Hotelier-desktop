# Form implementation generated from reading ui file 'GuestDetailsWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GuesDetailsWindow(object):
    def setupUi(self, GuesDetailsWindow):
        GuesDetailsWindow.setObjectName("GuesDetailsWindow")
        GuesDetailsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=GuesDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fname_lbl = QtWidgets.QLabel(parent=self.frame)
        self.fname_lbl.setObjectName("fname_lbl")
        self.verticalLayout.addWidget(self.fname_lbl)
        self.fname_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.fname_leddit.setObjectName("fname_leddit")
        self.verticalLayout.addWidget(self.fname_leddit)
        self.lname_lbl = QtWidgets.QLabel(parent=self.frame)
        self.lname_lbl.setObjectName("lname_lbl")
        self.verticalLayout.addWidget(self.lname_lbl)
        self.lame_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.lame_leddit.setObjectName("lame_leddit")
        self.verticalLayout.addWidget(self.lame_leddit)
        self.dob_lbl = QtWidgets.QLabel(parent=self.frame)
        self.dob_lbl.setObjectName("dob_lbl")
        self.verticalLayout.addWidget(self.dob_lbl)
        self.dob_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.dob_leddit.setObjectName("dob_leddit")
        self.verticalLayout.addWidget(self.dob_leddit)
        self.citizen_lbl = QtWidgets.QLabel(parent=self.frame)
        self.citizen_lbl.setObjectName("citizen_lbl")
        self.verticalLayout.addWidget(self.citizen_lbl)
        self.citizen_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.citizen_leddit.setObjectName("citizen_leddit")
        self.verticalLayout.addWidget(self.citizen_leddit)
        self.email_lbl = QtWidgets.QLabel(parent=self.frame)
        self.email_lbl.setObjectName("email_lbl")
        self.verticalLayout.addWidget(self.email_lbl)
        self.email_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.email_leddit.setObjectName("email_leddit")
        self.verticalLayout.addWidget(self.email_leddit)
        self.pnumber_lbl = QtWidgets.QLabel(parent=self.frame)
        self.pnumber_lbl.setObjectName("pnumber_lbl")
        self.verticalLayout.addWidget(self.pnumber_lbl)
        self.pnum_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.pnum_leddit.setObjectName("pnum_leddit")
        self.verticalLayout.addWidget(self.pnum_leddit)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.firstVisit_cbx = QtWidgets.QCheckBox(parent=self.frame_2)
        self.firstVisit_cbx.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.firstVisit_cbx.setObjectName("firstVisit_cbx")
        self.horizontalLayout_2.addWidget(self.firstVisit_cbx)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(676, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.close_btn = QtWidgets.QPushButton(parent=self.frame_3)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        GuesDetailsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=GuesDetailsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        GuesDetailsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=GuesDetailsWindow)
        self.statusbar.setObjectName("statusbar")
        GuesDetailsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GuesDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(GuesDetailsWindow)

    def retranslateUi(self, GuesDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        GuesDetailsWindow.setWindowTitle(_translate("GuesDetailsWindow", "Guest details"))
        self.fname_lbl.setText(_translate("GuesDetailsWindow", "First name"))
        self.lname_lbl.setText(_translate("GuesDetailsWindow", "Last name"))
        self.dob_lbl.setText(_translate("GuesDetailsWindow", "Date of birth"))
        self.citizen_lbl.setText(_translate("GuesDetailsWindow", "Citizenship"))
        self.email_lbl.setText(_translate("GuesDetailsWindow", "E-mail"))
        self.pnumber_lbl.setText(_translate("GuesDetailsWindow", "Phone number"))
        self.firstVisit_cbx.setText(_translate("GuesDetailsWindow", "First visit"))
        self.close_btn.setText(_translate("GuesDetailsWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GuesDetailsWindow = QtWidgets.QMainWindow()
    ui = Ui_GuesDetailsWindow()
    ui.setupUi(GuesDetailsWindow)
    GuesDetailsWindow.show()
    sys.exit(app.exec())
