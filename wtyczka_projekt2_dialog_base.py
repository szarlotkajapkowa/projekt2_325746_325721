# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_projekt2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wtyczka_projekt2DialogBase(object):
    def setupUi(self, wtyczka_projekt2DialogBase):
        wtyczka_projekt2DialogBase.setObjectName("wtyczka_projekt2DialogBase")
        wtyczka_projekt2DialogBase.resize(873, 562)
        self.button_box = QtWidgets.QDialogButtonBox(wtyczka_projekt2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(390, 480, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.layerComboBox = QtWidgets.QComboBox(wtyczka_projekt2DialogBase)
        self.layerComboBox.setGeometry(QtCore.QRect(500, 60, 211, 22))
        self.layerComboBox.setObjectName("layerComboBox")
        self.calculateAreaButton = QtWidgets.QPushButton(wtyczka_projekt2DialogBase)
        self.calculateAreaButton.setGeometry(QtCore.QRect(110, 300, 161, 31))
        self.calculateAreaButton.setObjectName("calculateAreaButton")
        self.calculateDifferenceButton = QtWidgets.QPushButton(wtyczka_projekt2DialogBase)
        self.calculateDifferenceButton.setGeometry(QtCore.QRect(110, 340, 161, 31))
        self.calculateDifferenceButton.setObjectName("calculateDifferenceButton")

        self.retranslateUi(wtyczka_projekt2DialogBase)
        self.button_box.accepted.connect(wtyczka_projekt2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(wtyczka_projekt2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(wtyczka_projekt2DialogBase)

    def retranslateUi(self, wtyczka_projekt2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        wtyczka_projekt2DialogBase.setWindowTitle(_translate("wtyczka_projekt2DialogBase", "wtyczka_projekt2"))
        self.calculateAreaButton.setText(_translate("wtyczka_projekt2DialogBase", "Oblicz pole"))
        self.calculateDifferenceButton.setText(_translate("wtyczka_projekt2DialogBase", "oblicz roznice wysokosci"))