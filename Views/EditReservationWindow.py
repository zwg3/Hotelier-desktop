# Form implementation generated from reading ui file 'EditReservationWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditResWindow(object):
    def setupUi(self, EditResWindow):
        EditResWindow.setObjectName("EditResWindow")
        EditResWindow.resize(1022, 867)
        self.centralwidget = QtWidgets.QWidget(parent=EditResWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(parent=self.frame_4)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.doa_lbl = QtWidgets.QLabel(parent=self.frame)
        self.doa_lbl.setObjectName("doa_lbl")
        self.verticalLayout.addWidget(self.doa_lbl)
        self.doa_daddit = QtWidgets.QDateEdit(parent=self.frame)
        self.doa_daddit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 27), QtCore.QTime(3, 0, 0)))
        self.doa_daddit.setCalendarPopup(True)
        self.doa_daddit.setObjectName("doa_daddit")
        self.verticalLayout.addWidget(self.doa_daddit)
        self.dod_lbl = QtWidgets.QLabel(parent=self.frame)
        self.dod_lbl.setObjectName("dod_lbl")
        self.verticalLayout.addWidget(self.dod_lbl)
        self.dod_daddit = QtWidgets.QDateEdit(parent=self.frame)
        self.dod_daddit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 27), QtCore.QTime(3, 0, 0)))
        self.dod_daddit.setCalendarPopup(True)
        self.dod_daddit.setObjectName("dod_daddit")
        self.verticalLayout.addWidget(self.dod_daddit)
        self.stay_lbl = QtWidgets.QLabel(parent=self.frame)
        self.stay_lbl.setObjectName("stay_lbl")
        self.verticalLayout.addWidget(self.stay_lbl)
        self.rate_lbl = QtWidgets.QLabel(parent=self.frame)
        self.rate_lbl.setObjectName("rate_lbl")
        self.verticalLayout.addWidget(self.rate_lbl)
        self.rate_leddit = QtWidgets.QLineEdit(parent=self.frame)
        self.rate_leddit.setObjectName("rate_leddit")
        self.verticalLayout.addWidget(self.rate_leddit)
        self.rateEdit_btn = QtWidgets.QPushButton(parent=self.frame)
        self.rateEdit_btn.setObjectName("rateEdit_btn")
        self.verticalLayout.addWidget(self.rateEdit_btn)
        self.payment_lbl = QtWidgets.QLabel(parent=self.frame)
        self.payment_lbl.setObjectName("payment_lbl")
        self.verticalLayout.addWidget(self.payment_lbl)
        self.payment_cbx = QtWidgets.QComboBox(parent=self.frame)
        self.payment_cbx.setObjectName("payment_cbx")
        self.verticalLayout.addWidget(self.payment_cbx)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.roomtype_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.roomtype_lbl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.roomtype_lbl.setObjectName("roomtype_lbl")
        self.verticalLayout_2.addWidget(self.roomtype_lbl)
        self.roomtype_cbox = QtWidgets.QComboBox(parent=self.frame_2)
        self.roomtype_cbox.setObjectName("roomtype_cbox")
        self.verticalLayout_2.addWidget(self.roomtype_cbox)
        self.rmNum_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.rmNum_lbl.setObjectName("rmNum_lbl")
        self.verticalLayout_2.addWidget(self.rmNum_lbl)
        self.rmNum_cbx = QtWidgets.QComboBox(parent=self.frame_2)
        self.rmNum_cbx.setObjectName("rmNum_cbx")
        self.verticalLayout_2.addWidget(self.rmNum_cbx)
        self.rmsAdded_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.rmsAdded_lbl.setObjectName("rmsAdded_lbl")
        self.verticalLayout_2.addWidget(self.rmsAdded_lbl)
        self.resRms_twidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.resRms_twidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resRms_twidget.setObjectName("resRms_twidget")
        self.resRms_twidget.setColumnCount(0)
        self.resRms_twidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.resRms_twidget)
        self.selectGuest_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.selectGuest_btn.setObjectName("selectGuest_btn")
        self.verticalLayout_2.addWidget(self.selectGuest_btn)
        self.drm_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.drm_btn.setObjectName("drm_btn")
        self.verticalLayout_2.addWidget(self.drm_btn)
        self.comment_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.comment_lbl.setObjectName("comment_lbl")
        self.verticalLayout_2.addWidget(self.comment_lbl)
        self.comment_leddit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.comment_leddit.setObjectName("comment_leddit")
        self.verticalLayout_2.addWidget(self.comment_leddit)
        self.total_lbl = QtWidgets.QLabel(parent=self.frame_2)
        self.total_lbl.setObjectName("total_lbl")
        self.verticalLayout_2.addWidget(self.total_lbl)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.resId_lbl = QtWidgets.QLabel(parent=self.frame_3)
        self.resId_lbl.setObjectName("resId_lbl")
        self.verticalLayout_3.addWidget(self.resId_lbl)
        self.create_btn = QtWidgets.QPushButton(parent=self.frame_3)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout_3.addWidget(self.create_btn)
        self.exit_Btn = QtWidgets.QPushButton(parent=self.frame_3)
        self.exit_Btn.setObjectName("exit_Btn")
        self.verticalLayout_3.addWidget(self.exit_Btn)
        self.horizontalLayout.addWidget(self.frame_3)
        EditResWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditResWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 22))
        self.menubar.setObjectName("menubar")
        EditResWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditResWindow)
        self.statusbar.setObjectName("statusbar")
        EditResWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditResWindow)
        QtCore.QMetaObject.connectSlotsByName(EditResWindow)

    def retranslateUi(self, EditResWindow):
        _translate = QtCore.QCoreApplication.translate
        EditResWindow.setWindowTitle(_translate("EditResWindow", "Edit reservation"))
        self.doa_lbl.setText(_translate("EditResWindow", "Date of arrival"))
        self.dod_lbl.setText(_translate("EditResWindow", "Date of departure"))
        self.stay_lbl.setText(_translate("EditResWindow", "Stay duration:"))
        self.rate_lbl.setText(_translate("EditResWindow", "Rate"))
        self.rate_leddit.setText(_translate("EditResWindow", "0"))
        self.rateEdit_btn.setText(_translate("EditResWindow", "Set daily rate"))
        self.payment_lbl.setText(_translate("EditResWindow", "Method of payment"))
        self.roomtype_lbl.setText(_translate("EditResWindow", "Room type"))
        self.rmNum_lbl.setText(_translate("EditResWindow", "Room number"))
        self.rmsAdded_lbl.setText(_translate("EditResWindow", "Reserved rooms"))
        self.selectGuest_btn.setText(_translate("EditResWindow", "Add guest"))
        self.drm_btn.setText(_translate("EditResWindow", "Remove guest"))
        self.comment_lbl.setText(_translate("EditResWindow", "Commentary"))
        self.total_lbl.setText(_translate("EditResWindow", "Total cost:"))
        self.resId_lbl.setText(_translate("EditResWindow", "Reservation id"))
        self.create_btn.setText(_translate("EditResWindow", "Save changes"))
        self.exit_Btn.setText(_translate("EditResWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditResWindow = QtWidgets.QMainWindow()
    ui = Ui_EditResWindow()
    ui.setupUi(EditResWindow)
    EditResWindow.show()
    sys.exit(app.exec())
