# Form implementation generated from reading ui file 'AddRoleWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddRoleWindow(object):
    def setupUi(self, AddRoleWindow):
        AddRoleWindow.setObjectName("AddRoleWindow")
        AddRoleWindow.resize(341, 276)
        self.centralwidget = QtWidgets.QWidget(parent=AddRoleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rtitle_lbl = QtWidgets.QLabel(parent=self.frame)
        self.rtitle_lbl.setObjectName("rtitle_lbl")
        self.verticalLayout.addWidget(self.rtitle_lbl)
        self.rtitle_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.rtitle_leddit.setObjectName("rtitle_leddit")
        self.verticalLayout.addWidget(self.rtitle_leddit)
        self.setAccess_lbl = QtWidgets.QLabel(parent=self.frame)
        self.setAccess_lbl.setObjectName("setAccess_lbl")
        self.verticalLayout.addWidget(self.setAccess_lbl)
        self.setAccess_cbox = QtWidgets.QComboBox(parent=self.frame)
        self.setAccess_cbox.setObjectName("setAccess_cbox")
        self.verticalLayout.addWidget(self.setAccess_cbox)
        self.rdesc_lbl = QtWidgets.QLabel(parent=self.frame)
        self.rdesc_lbl.setObjectName("rdesc_lbl")
        self.verticalLayout.addWidget(self.rdesc_lbl)
        self.rdesc_lbl_2 = QtWidgets.QTextEdit(parent=self.frame)
        self.rdesc_lbl_2.setObjectName("rdesc_lbl_2")
        self.verticalLayout.addWidget(self.rdesc_lbl_2)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.frame)
        AddRoleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AddRoleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 22))
        self.menubar.setObjectName("menubar")
        AddRoleWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AddRoleWindow)
        self.statusbar.setObjectName("statusbar")
        AddRoleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddRoleWindow)
        QtCore.QMetaObject.connectSlotsByName(AddRoleWindow)

    def retranslateUi(self, AddRoleWindow):
        _translate = QtCore.QCoreApplication.translate
        AddRoleWindow.setWindowTitle(_translate("AddRoleWindow", "Adding role"))
        self.rtitle_lbl.setText(_translate("AddRoleWindow", "Role title"))
        self.setAccess_lbl.setText(_translate("AddRoleWindow", "Access level"))
        self.rdesc_lbl.setText(_translate("AddRoleWindow", "Role description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddRoleWindow = QtWidgets.QMainWindow()
    ui = Ui_AddRoleWindow()
    ui.setupUi(AddRoleWindow)
    AddRoleWindow.show()
    sys.exit(app.exec())
