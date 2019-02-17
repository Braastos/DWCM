# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InventoryGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventoryManager(object):
    def setupUi(self, inventoryManager):
        inventoryManager.setObjectName("inventoryManager")
        inventoryManager.resize(771, 720)
        font = QtGui.QFont()
        font.setPointSize(15)
        inventoryManager.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dwlogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inventoryManager.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(inventoryManager)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.plusOneButton = QtWidgets.QPushButton(inventoryManager)
        self.plusOneButton.setToolTipDuration(0)
        self.plusOneButton.setObjectName("plusOneButton")
        self.gridLayout.addWidget(self.plusOneButton, 1, 3, 1, 1)
        self.minusOneButton = QtWidgets.QPushButton(inventoryManager)
        self.minusOneButton.setToolTipDuration(0)
        self.minusOneButton.setObjectName("minusOneButton")
        self.gridLayout.addWidget(self.minusOneButton, 1, 2, 1, 1)
        self.erstellenButton = QtWidgets.QPushButton(inventoryManager)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.erstellenButton.setFont(font)
        self.erstellenButton.setToolTipDuration(0)
        self.erstellenButton.setObjectName("erstellenButton")
        self.gridLayout.addWidget(self.erstellenButton, 1, 0, 1, 1)
        self.plusFiveButton = QtWidgets.QPushButton(inventoryManager)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plusFiveButton.setFont(font)
        self.plusFiveButton.setToolTipDuration(0)
        self.plusFiveButton.setObjectName("plusFiveButton")
        self.gridLayout.addWidget(self.plusFiveButton, 1, 4, 1, 1)
        self.minusFiveButton = QtWidgets.QPushButton(inventoryManager)
        self.minusFiveButton.setToolTipDuration(0)
        self.minusFiveButton.setObjectName("minusFiveButton")
        self.gridLayout.addWidget(self.minusFiveButton, 1, 1, 1, 1)
        self.editButton = QtWidgets.QPushButton(inventoryManager)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 1, 5, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(inventoryManager)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 751, 662))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inventoryView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.inventoryView.setFont(font)
        self.inventoryView.setAlternatingRowColors(True)
        self.inventoryView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.inventoryView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.inventoryView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.inventoryView.setObjectName("inventoryView")
        self.gridLayout_2.addWidget(self.inventoryView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 6)

        self.retranslateUi(inventoryManager)
        QtCore.QMetaObject.connectSlotsByName(inventoryManager)

    def retranslateUi(self, inventoryManager):
        _translate = QtCore.QCoreApplication.translate
        inventoryManager.setWindowTitle(_translate("inventoryManager", "Dungeon World Inventory Manager"))
        self.plusOneButton.setToolTip(_translate("inventoryManager", "Erhöht die Menge des aktuelle ausgewähltem Items um 1"))
        self.plusOneButton.setText(_translate("inventoryManager", "+1"))
        self.minusOneButton.setToolTip(_translate("inventoryManager", "Verringert die Menge des aktuelle ausgewähltem Items um 1"))
        self.minusOneButton.setText(_translate("inventoryManager", "-1"))
        self.erstellenButton.setToolTip(_translate("inventoryManager", "Öffnet ein Fenster um ein neues Item zu erstellen"))
        self.erstellenButton.setText(_translate("inventoryManager", "Erstellen"))
        self.plusFiveButton.setToolTip(_translate("inventoryManager", "Erhöht die Menge des aktuelle ausgewähltem Items um 5"))
        self.plusFiveButton.setText(_translate("inventoryManager", "+5"))
        self.minusFiveButton.setToolTip(_translate("inventoryManager", "Verringert die Menge des aktuelle ausgewähltem Items um 5"))
        self.minusFiveButton.setText(_translate("inventoryManager", "-5"))
        self.editButton.setText(_translate("inventoryManager", "Bearbeiten"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryManager = QtWidgets.QDialog()
    ui = Ui_inventoryManager()
    ui.setupUi(inventoryManager)
    inventoryManager.show()
    sys.exit(app.exec_())

