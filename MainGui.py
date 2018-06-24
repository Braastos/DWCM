# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DungeonWorldCharakter(object):
    def setupUi(self, DungeonWorldCharakter):
        DungeonWorldCharakter.setObjectName("DungeonWorldCharakter")
        DungeonWorldCharakter.resize(573, 695)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        DungeonWorldCharakter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dwlogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DungeonWorldCharakter.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DungeonWorldCharakter)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 661))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.stats = QtWidgets.QWidget()
        self.stats.setObjectName("stats")
        self.ep = QtWidgets.QLabel(self.stats)
        self.ep.setGeometry(QtCore.QRect(230, 70, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ep.setFont(font)
        self.ep.setObjectName("ep")
        self.geschickPunkte = QtWidgets.QSpinBox(self.stats)
        self.geschickPunkte.setGeometry(QtCore.QRect(10, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.geschickPunkte.setFont(font)
        self.geschickPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.geschickPunkte.setMaximum(18)
        self.geschickPunkte.setProperty("value", 0)
        self.geschickPunkte.setObjectName("geschickPunkte")
        self.schaden = QtWidgets.QLabel(self.stats)
        self.schaden.setGeometry(QtCore.QRect(210, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.schaden.setFont(font)
        self.schaden.setObjectName("schaden")
        self.charismaPunkte = QtWidgets.QSpinBox(self.stats)
        self.charismaPunkte.setGeometry(QtCore.QRect(10, 420, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.charismaPunkte.setFont(font)
        self.charismaPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.charismaPunkte.setMaximum(18)
        self.charismaPunkte.setProperty("value", 0)
        self.charismaPunkte.setObjectName("charismaPunkte")
        self.epPunkte = QtWidgets.QSpinBox(self.stats)
        self.epPunkte.setGeometry(QtCore.QRect(280, 70, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.epPunkte.setFont(font)
        self.epPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.epPunkte.setProperty("value", 7)
        self.epPunkte.setObjectName("epPunkte")
        self.weisheitPunkte = QtWidgets.QSpinBox(self.stats)
        self.weisheitPunkte.setGeometry(QtCore.QRect(10, 360, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.weisheitPunkte.setFont(font)
        self.weisheitPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.weisheitPunkte.setMaximum(18)
        self.weisheitPunkte.setProperty("value", 0)
        self.weisheitPunkte.setObjectName("weisheitPunkte")
        self.stufePunkte = QtWidgets.QSpinBox(self.stats)
        self.stufePunkte.setGeometry(QtCore.QRect(130, 70, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.stufePunkte.setFont(font)
        self.stufePunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.stufePunkte.setMaximum(10)
        self.stufePunkte.setProperty("value", 2)
        self.stufePunkte.setObjectName("stufePunkte")
        self.charisma = QtWidgets.QLabel(self.stats)
        self.charisma.setGeometry(QtCore.QRect(110, 420, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.charisma.setFont(font)
        self.charisma.setObjectName("charisma")
        self.konstitution = QtWidgets.QLabel(self.stats)
        self.konstitution.setGeometry(QtCore.QRect(110, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.konstitution.setFont(font)
        self.konstitution.setObjectName("konstitution")
        self.intelligenzPunkte = QtWidgets.QSpinBox(self.stats)
        self.intelligenzPunkte.setGeometry(QtCore.QRect(10, 300, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.intelligenzPunkte.setFont(font)
        self.intelligenzPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.intelligenzPunkte.setMaximum(18)
        self.intelligenzPunkte.setProperty("value", 0)
        self.intelligenzPunkte.setObjectName("intelligenzPunkte")
        self.stufe = QtWidgets.QLabel(self.stats)
        self.stufe.setGeometry(QtCore.QRect(10, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.stufe.setFont(font)
        self.stufe.setObjectName("stufe")
        self.geschick = QtWidgets.QLabel(self.stats)
        self.geschick.setGeometry(QtCore.QRect(110, 180, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.geschick.setFont(font)
        self.geschick.setObjectName("geschick")
        self.schadenPunkte = QtWidgets.QLabel(self.stats)
        self.schadenPunkte.setGeometry(QtCore.QRect(340, 480, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.schadenPunkte.setFont(font)
        self.schadenPunkte.setObjectName("schadenPunkte")
        self.staerkePunkte = QtWidgets.QSpinBox(self.stats)
        self.staerkePunkte.setGeometry(QtCore.QRect(10, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.staerkePunkte.setFont(font)
        self.staerkePunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.staerkePunkte.setMinimum(0)
        self.staerkePunkte.setMaximum(18)
        self.staerkePunkte.setProperty("value", 0)
        self.staerkePunkte.setObjectName("staerkePunkte")
        self.staerke = QtWidgets.QLabel(self.stats)
        self.staerke.setGeometry(QtCore.QRect(110, 120, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.staerke.setFont(font)
        self.staerke.setObjectName("staerke")
        self.konstitutionPunkte = QtWidgets.QSpinBox(self.stats)
        self.konstitutionPunkte.setGeometry(QtCore.QRect(10, 240, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.konstitutionPunkte.setFont(font)
        self.konstitutionPunkte.setAlignment(QtCore.Qt.AlignCenter)
        self.konstitutionPunkte.setMaximum(18)
        self.konstitutionPunkte.setProperty("value", 0)
        self.konstitutionPunkte.setObjectName("konstitutionPunkte")
        self.Name = QtWidgets.QTextEdit(self.stats)
        self.Name.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.weisheit = QtWidgets.QLabel(self.stats)
        self.weisheit.setGeometry(QtCore.QRect(110, 360, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.weisheit.setFont(font)
        self.weisheit.setObjectName("weisheit")
        self.intelligenz = QtWidgets.QLabel(self.stats)
        self.intelligenz.setGeometry(QtCore.QRect(110, 300, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.intelligenz.setFont(font)
        self.intelligenz.setObjectName("intelligenz")
        self.ruestung = QtWidgets.QLabel(self.stats)
        self.ruestung.setGeometry(QtCore.QRect(10, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ruestung.setFont(font)
        self.ruestung.setObjectName("ruestung")
        self.lebenAktuellText = QtWidgets.QLabel(self.stats)
        self.lebenAktuellText.setGeometry(QtCore.QRect(210, 530, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lebenAktuellText.setFont(font)
        self.lebenAktuellText.setObjectName("lebenAktuellText")
        self.lebenText = QtWidgets.QLabel(self.stats)
        self.lebenText.setGeometry(QtCore.QRect(10, 530, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lebenText.setFont(font)
        self.lebenText.setObjectName("lebenText")
        self.lebenAktuell = QtWidgets.QSpinBox(self.stats)
        self.lebenAktuell.setGeometry(QtCore.QRect(340, 530, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lebenAktuell.setFont(font)
        self.lebenAktuell.setAlignment(QtCore.Qt.AlignCenter)
        self.lebenAktuell.setObjectName("lebenAktuell")
        self.lebenMax = QtWidgets.QLabel(self.stats)
        self.lebenMax.setGeometry(QtCore.QRect(140, 530, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lebenMax.setFont(font)
        self.lebenMax.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lebenMax.setObjectName("lebenMax")
        self.belastungAktuellText = QtWidgets.QLabel(self.stats)
        self.belastungAktuellText.setGeometry(QtCore.QRect(210, 580, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.belastungAktuellText.setFont(font)
        self.belastungAktuellText.setObjectName("belastungAktuellText")
        self.belastungText = QtWidgets.QLabel(self.stats)
        self.belastungText.setGeometry(QtCore.QRect(10, 580, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.belastungText.setFont(font)
        self.belastungText.setObjectName("belastungText")
        self.belastungMax = QtWidgets.QLabel(self.stats)
        self.belastungMax.setGeometry(QtCore.QRect(140, 580, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.belastungMax.setFont(font)
        self.belastungMax.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.belastungMax.setObjectName("belastungMax")
        self.staerkeBonus = QtWidgets.QLabel(self.stats)
        self.staerkeBonus.setGeometry(QtCore.QRect(350, 120, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.staerkeBonus.setFont(font)
        self.staerkeBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.staerkeBonus.setObjectName("staerkeBonus")
        self.geschickBonus = QtWidgets.QLabel(self.stats)
        self.geschickBonus.setGeometry(QtCore.QRect(350, 180, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.geschickBonus.setFont(font)
        self.geschickBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.geschickBonus.setObjectName("geschickBonus")
        self.konstitutionBonus = QtWidgets.QLabel(self.stats)
        self.konstitutionBonus.setGeometry(QtCore.QRect(350, 240, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.konstitutionBonus.setFont(font)
        self.konstitutionBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.konstitutionBonus.setObjectName("konstitutionBonus")
        self.intelligenzBonus = QtWidgets.QLabel(self.stats)
        self.intelligenzBonus.setGeometry(QtCore.QRect(350, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.intelligenzBonus.setFont(font)
        self.intelligenzBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.intelligenzBonus.setObjectName("intelligenzBonus")
        self.weisheitBonus = QtWidgets.QLabel(self.stats)
        self.weisheitBonus.setGeometry(QtCore.QRect(350, 360, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.weisheitBonus.setFont(font)
        self.weisheitBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weisheitBonus.setObjectName("weisheitBonus")
        self.charismaBonus = QtWidgets.QLabel(self.stats)
        self.charismaBonus.setGeometry(QtCore.QRect(350, 420, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.charismaBonus.setFont(font)
        self.charismaBonus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.charismaBonus.setObjectName("charismaBonus")
        self.klasse = QtWidgets.QLabel(self.stats)
        self.klasse.setGeometry(QtCore.QRect(360, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.klasse.setFont(font)
        self.klasse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.klasse.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.klasse.setObjectName("klasse")
        self.klassenAuswahl = QtWidgets.QComboBox(self.stats)
        self.klassenAuswahl.setGeometry(QtCore.QRect(360, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.klassenAuswahl.setFont(font)
        self.klassenAuswahl.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.klassenAuswahl.setObjectName("klassenAuswahl")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.klassenAuswahl.addItem("")
        self.AktivQuests = QtWidgets.QCheckBox(self.stats)
        self.AktivQuests.setGeometry(QtCore.QRect(430, 530, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.AktivQuests.setFont(font)
        self.AktivQuests.setObjectName("AktivQuests")
        self.belastungAktuell = QtWidgets.QLabel(self.stats)
        self.belastungAktuell.setGeometry(QtCore.QRect(340, 580, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.belastungAktuell.setFont(font)
        self.belastungAktuell.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.belastungAktuell.setAlignment(QtCore.Qt.AlignCenter)
        self.belastungAktuell.setObjectName("belastungAktuell")
        self.ruestungPunkte = QtWidgets.QLabel(self.stats)
        self.ruestungPunkte.setGeometry(QtCore.QRect(140, 480, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ruestungPunkte.setFont(font)
        self.ruestungPunkte.setObjectName("ruestungPunkte")
        self.schadenWert = QtWidgets.QLabel(self.stats)
        self.schadenWert.setGeometry(QtCore.QRect(480, 480, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.schadenWert.setFont(font)
        self.schadenWert.setObjectName("schadenWert")
        self.tabWidget.addTab(self.stats, "")
        self.inventory = QtWidgets.QWidget()
        self.inventory.setObjectName("inventory")
        self.muenzenText = QtWidgets.QLabel(self.inventory)
        self.muenzenText.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.muenzenText.setFont(font)
        self.muenzenText.setObjectName("muenzenText")
        self.muenzen = QtWidgets.QSpinBox(self.inventory)
        self.muenzen.setGeometry(QtCore.QRect(120, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.muenzen.setFont(font)
        self.muenzen.setAlignment(QtCore.Qt.AlignCenter)
        self.muenzen.setMaximum(99999999)
        self.muenzen.setProperty("value", 0)
        self.muenzen.setObjectName("muenzen")
        self.edelsteine = QtWidgets.QSpinBox(self.inventory)
        self.edelsteine.setGeometry(QtCore.QRect(460, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.edelsteine.setFont(font)
        self.edelsteine.setAlignment(QtCore.Qt.AlignCenter)
        self.edelsteine.setMaximum(999)
        self.edelsteine.setProperty("value", 0)
        self.edelsteine.setObjectName("edelsteine")
        self.edelsteineText = QtWidgets.QLabel(self.inventory)
        self.edelsteineText.setGeometry(QtCore.QRect(310, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.edelsteineText.setFont(font)
        self.edelsteineText.setObjectName("edelsteineText")
        self.feldrationenText = QtWidgets.QLabel(self.inventory)
        self.feldrationenText.setGeometry(QtCore.QRect(10, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.feldrationenText.setFont(font)
        self.feldrationenText.setObjectName("feldrationenText")
        self.gewichtText = QtWidgets.QLabel(self.inventory)
        self.gewichtText.setGeometry(QtCore.QRect(390, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gewichtText.setFont(font)
        self.gewichtText.setObjectName("gewichtText")
        self.feldrationenMenge = QtWidgets.QSpinBox(self.inventory)
        self.feldrationenMenge.setGeometry(QtCore.QRect(310, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.feldrationenMenge.setFont(font)
        self.feldrationenMenge.setAlignment(QtCore.Qt.AlignCenter)
        self.feldrationenMenge.setMaximum(99)
        self.feldrationenMenge.setProperty("value", 0)
        self.feldrationenMenge.setObjectName("feldrationenMenge")
        self.feldrationenGewicht = QtWidgets.QLabel(self.inventory)
        self.feldrationenGewicht.setGeometry(QtCore.QRect(500, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.feldrationenGewicht.setFont(font)
        self.feldrationenGewicht.setAlignment(QtCore.Qt.AlignCenter)
        self.feldrationenGewicht.setObjectName("feldrationenGewicht")
        self.abenteuerausruestungText = QtWidgets.QLabel(self.inventory)
        self.abenteuerausruestungText.setGeometry(QtCore.QRect(10, 110, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.abenteuerausruestungText.setFont(font)
        self.abenteuerausruestungText.setObjectName("abenteuerausruestungText")
        self.heiltraenkeText = QtWidgets.QLabel(self.inventory)
        self.heiltraenkeText.setGeometry(QtCore.QRect(10, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.heiltraenkeText.setFont(font)
        self.heiltraenkeText.setObjectName("heiltraenkeText")
        self.abenteuerausruestungGewicht = QtWidgets.QLabel(self.inventory)
        self.abenteuerausruestungGewicht.setGeometry(QtCore.QRect(500, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.abenteuerausruestungGewicht.setFont(font)
        self.abenteuerausruestungGewicht.setAlignment(QtCore.Qt.AlignCenter)
        self.abenteuerausruestungGewicht.setObjectName("abenteuerausruestungGewicht")
        self.abenteuerausruestungMenge = QtWidgets.QSpinBox(self.inventory)
        self.abenteuerausruestungMenge.setGeometry(QtCore.QRect(310, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.abenteuerausruestungMenge.setFont(font)
        self.abenteuerausruestungMenge.setAlignment(QtCore.Qt.AlignCenter)
        self.abenteuerausruestungMenge.setMaximum(99)
        self.abenteuerausruestungMenge.setProperty("value", 0)
        self.abenteuerausruestungMenge.setObjectName("abenteuerausruestungMenge")
        self.gewichtText_2 = QtWidgets.QLabel(self.inventory)
        self.gewichtText_2.setGeometry(QtCore.QRect(390, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gewichtText_2.setFont(font)
        self.gewichtText_2.setObjectName("gewichtText_2")
        self.heiltraenkeGewicht = QtWidgets.QLabel(self.inventory)
        self.heiltraenkeGewicht.setGeometry(QtCore.QRect(500, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.heiltraenkeGewicht.setFont(font)
        self.heiltraenkeGewicht.setAlignment(QtCore.Qt.AlignCenter)
        self.heiltraenkeGewicht.setObjectName("heiltraenkeGewicht")
        self.heiltraenkeMenge = QtWidgets.QSpinBox(self.inventory)
        self.heiltraenkeMenge.setGeometry(QtCore.QRect(310, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.heiltraenkeMenge.setFont(font)
        self.heiltraenkeMenge.setAlignment(QtCore.Qt.AlignCenter)
        self.heiltraenkeMenge.setMaximum(99)
        self.heiltraenkeMenge.setProperty("value", 0)
        self.heiltraenkeMenge.setObjectName("heiltraenkeMenge")
        self.gewichtText_3 = QtWidgets.QLabel(self.inventory)
        self.gewichtText_3.setGeometry(QtCore.QRect(390, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gewichtText_3.setFont(font)
        self.gewichtText_3.setObjectName("gewichtText_3")
        self.rucksackButton = QtWidgets.QPushButton(self.inventory)
        self.rucksackButton.setGeometry(QtCore.QRect(200, 590, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rucksackButton.setFont(font)
        self.rucksackButton.setToolTipDuration(0)
        self.rucksackButton.setObjectName("rucksackButton")
        self.buendelPfeileMenge = QtWidgets.QSpinBox(self.inventory)
        self.buendelPfeileMenge.setGeometry(QtCore.QRect(310, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.buendelPfeileMenge.setFont(font)
        self.buendelPfeileMenge.setAlignment(QtCore.Qt.AlignCenter)
        self.buendelPfeileMenge.setMaximum(99)
        self.buendelPfeileMenge.setProperty("value", 0)
        self.buendelPfeileMenge.setObjectName("buendelPfeileMenge")
        self.buendelpfeileText = QtWidgets.QLabel(self.inventory)
        self.buendelpfeileText.setGeometry(QtCore.QRect(10, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.buendelpfeileText.setFont(font)
        self.buendelpfeileText.setObjectName("buendelpfeileText")
        self.gewichtText_4 = QtWidgets.QLabel(self.inventory)
        self.gewichtText_4.setGeometry(QtCore.QRect(390, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gewichtText_4.setFont(font)
        self.gewichtText_4.setObjectName("gewichtText_4")
        self.buendelPfeileGewicht = QtWidgets.QLabel(self.inventory)
        self.buendelPfeileGewicht.setGeometry(QtCore.QRect(500, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.buendelPfeileGewicht.setFont(font)
        self.buendelPfeileGewicht.setAlignment(QtCore.Qt.AlignCenter)
        self.buendelPfeileGewicht.setObjectName("buendelPfeileGewicht")
        self.tabWidget.addTab(self.inventory, "")
        self.boni = QtWidgets.QWidget()
        self.boni.setObjectName("boni")
        self.charismaBonusGM = QtWidgets.QSpinBox(self.boni)
        self.charismaBonusGM.setGeometry(QtCore.QRect(490, 310, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.charismaBonusGM.setFont(font)
        self.charismaBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.charismaBonusGM.setMinimum(-18)
        self.charismaBonusGM.setMaximum(18)
        self.charismaBonusGM.setProperty("value", 0)
        self.charismaBonusGM.setObjectName("charismaBonusGM")
        self.geschickBonusGM = QtWidgets.QSpinBox(self.boni)
        self.geschickBonusGM.setGeometry(QtCore.QRect(490, 70, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.geschickBonusGM.setFont(font)
        self.geschickBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.geschickBonusGM.setMinimum(-18)
        self.geschickBonusGM.setMaximum(18)
        self.geschickBonusGM.setProperty("value", 0)
        self.geschickBonusGM.setObjectName("geschickBonusGM")
        self.weisheitBonusGM = QtWidgets.QSpinBox(self.boni)
        self.weisheitBonusGM.setGeometry(QtCore.QRect(490, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.weisheitBonusGM.setFont(font)
        self.weisheitBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.weisheitBonusGM.setMinimum(-18)
        self.weisheitBonusGM.setMaximum(18)
        self.weisheitBonusGM.setProperty("value", 0)
        self.weisheitBonusGM.setObjectName("weisheitBonusGM")
        self.intelligenzBonusGM = QtWidgets.QSpinBox(self.boni)
        self.intelligenzBonusGM.setGeometry(QtCore.QRect(490, 190, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.intelligenzBonusGM.setFont(font)
        self.intelligenzBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.intelligenzBonusGM.setMinimum(-18)
        self.intelligenzBonusGM.setMaximum(18)
        self.intelligenzBonusGM.setProperty("value", 0)
        self.intelligenzBonusGM.setObjectName("intelligenzBonusGM")
        self.konstitutionBonusGM = QtWidgets.QSpinBox(self.boni)
        self.konstitutionBonusGM.setGeometry(QtCore.QRect(490, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.konstitutionBonusGM.setFont(font)
        self.konstitutionBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.konstitutionBonusGM.setMinimum(-18)
        self.konstitutionBonusGM.setMaximum(18)
        self.konstitutionBonusGM.setProperty("value", 0)
        self.konstitutionBonusGM.setObjectName("konstitutionBonusGM")
        self.schadenBonus = QtWidgets.QSpinBox(self.boni)
        self.schadenBonus.setGeometry(QtCore.QRect(490, 370, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.schadenBonus.setFont(font)
        self.schadenBonus.setAlignment(QtCore.Qt.AlignCenter)
        self.schadenBonus.setMinimum(-18)
        self.schadenBonus.setMaximum(18)
        self.schadenBonus.setProperty("value", 0)
        self.schadenBonus.setObjectName("schadenBonus")
        self.staerkeBonusGM = QtWidgets.QSpinBox(self.boni)
        self.staerkeBonusGM.setGeometry(QtCore.QRect(490, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.staerkeBonusGM.setFont(font)
        self.staerkeBonusGM.setAlignment(QtCore.Qt.AlignCenter)
        self.staerkeBonusGM.setMinimum(-18)
        self.staerkeBonusGM.setMaximum(18)
        self.staerkeBonusGM.setProperty("value", 0)
        self.staerkeBonusGM.setObjectName("staerkeBonusGM")
        self.geschick_2 = QtWidgets.QLabel(self.boni)
        self.geschick_2.setGeometry(QtCore.QRect(10, 70, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.geschick_2.setFont(font)
        self.geschick_2.setObjectName("geschick_2")
        self.weisheit_2 = QtWidgets.QLabel(self.boni)
        self.weisheit_2.setGeometry(QtCore.QRect(10, 250, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.weisheit_2.setFont(font)
        self.weisheit_2.setObjectName("weisheit_2")
        self.schaden_2 = QtWidgets.QLabel(self.boni)
        self.schaden_2.setGeometry(QtCore.QRect(10, 370, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.schaden_2.setFont(font)
        self.schaden_2.setObjectName("schaden_2")
        self.staerke_2 = QtWidgets.QLabel(self.boni)
        self.staerke_2.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.staerke_2.setFont(font)
        self.staerke_2.setObjectName("staerke_2")
        self.charisma_2 = QtWidgets.QLabel(self.boni)
        self.charisma_2.setGeometry(QtCore.QRect(10, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.charisma_2.setFont(font)
        self.charisma_2.setObjectName("charisma_2")
        self.ruestung_2 = QtWidgets.QLabel(self.boni)
        self.ruestung_2.setGeometry(QtCore.QRect(10, 430, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ruestung_2.setFont(font)
        self.ruestung_2.setObjectName("ruestung_2")
        self.intelligenz_2 = QtWidgets.QLabel(self.boni)
        self.intelligenz_2.setGeometry(QtCore.QRect(10, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.intelligenz_2.setFont(font)
        self.intelligenz_2.setObjectName("intelligenz_2")
        self.konstitution_2 = QtWidgets.QLabel(self.boni)
        self.konstitution_2.setGeometry(QtCore.QRect(10, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.konstitution_2.setFont(font)
        self.konstitution_2.setObjectName("konstitution_2")
        self.ruestungBonus = QtWidgets.QSpinBox(self.boni)
        self.ruestungBonus.setGeometry(QtCore.QRect(490, 430, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ruestungBonus.setFont(font)
        self.ruestungBonus.setAlignment(QtCore.Qt.AlignCenter)
        self.ruestungBonus.setMinimum(-18)
        self.ruestungBonus.setMaximum(18)
        self.ruestungBonus.setProperty("value", 0)
        self.ruestungBonus.setObjectName("ruestungBonus")
        self.tabWidget.addTab(self.boni, "")
        DungeonWorldCharakter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DungeonWorldCharakter)
        self.statusbar.setObjectName("statusbar")
        DungeonWorldCharakter.setStatusBar(self.statusbar)
        self.actionLaden = QtWidgets.QAction(DungeonWorldCharakter)
        self.actionLaden.setObjectName("actionLaden")
        self.actionInventarloeschen = QtWidgets.QAction(DungeonWorldCharakter)
        self.actionInventarloeschen.setObjectName("actionInventarloeschen")

        self.retranslateUi(DungeonWorldCharakter)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DungeonWorldCharakter)

    def retranslateUi(self, DungeonWorldCharakter):
        _translate = QtCore.QCoreApplication.translate
        DungeonWorldCharakter.setWindowTitle(_translate("DungeonWorldCharakter", "Dungeon World Charakter Manager"))
        self.ep.setText(_translate("DungeonWorldCharakter", "EP"))
        self.schaden.setText(_translate("DungeonWorldCharakter", "Schaden"))
        self.charisma.setText(_translate("DungeonWorldCharakter", "Charisma"))
        self.konstitution.setText(_translate("DungeonWorldCharakter", "Konstitution"))
        self.stufe.setText(_translate("DungeonWorldCharakter", "Stufe"))
        self.geschick.setText(_translate("DungeonWorldCharakter", "Geschick"))
        self.schadenPunkte.setText(_translate("DungeonWorldCharakter", "W10"))
        self.staerke.setText(_translate("DungeonWorldCharakter", "Stärke"))
        self.Name.setToolTip(_translate("DungeonWorldCharakter", "Name"))
        self.Name.setPlaceholderText(_translate("DungeonWorldCharakter", "Name"))
        self.weisheit.setText(_translate("DungeonWorldCharakter", "Weisheit"))
        self.intelligenz.setText(_translate("DungeonWorldCharakter", "Intelligenz"))
        self.ruestung.setText(_translate("DungeonWorldCharakter", "Rüstung"))
        self.lebenAktuellText.setText(_translate("DungeonWorldCharakter", "Aktuell"))
        self.lebenText.setText(_translate("DungeonWorldCharakter", "Leben"))
        self.lebenMax.setText(_translate("DungeonWorldCharakter", "0"))
        self.belastungAktuellText.setText(_translate("DungeonWorldCharakter", "Aktuell"))
        self.belastungText.setText(_translate("DungeonWorldCharakter", "Belastung"))
        self.belastungMax.setText(_translate("DungeonWorldCharakter", "0"))
        self.staerkeBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.geschickBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.konstitutionBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.intelligenzBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.weisheitBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.charismaBonus.setText(_translate("DungeonWorldCharakter", "0"))
        self.klasse.setText(_translate("DungeonWorldCharakter", "Klasse"))
        self.klassenAuswahl.setItemText(0, _translate("DungeonWorldCharakter", "Barbar"))
        self.klassenAuswahl.setItemText(1, _translate("DungeonWorldCharakter", "Barde"))
        self.klassenAuswahl.setItemText(2, _translate("DungeonWorldCharakter", "Druide"))
        self.klassenAuswahl.setItemText(3, _translate("DungeonWorldCharakter", "Kämpfer"))
        self.klassenAuswahl.setItemText(4, _translate("DungeonWorldCharakter", "Kleriker"))
        self.klassenAuswahl.setItemText(5, _translate("DungeonWorldCharakter", "Paladin"))
        self.klassenAuswahl.setItemText(6, _translate("DungeonWorldCharakter", "Schurke"))
        self.klassenAuswahl.setItemText(7, _translate("DungeonWorldCharakter", "Waldläufer"))
        self.klassenAuswahl.setItemText(8, _translate("DungeonWorldCharakter", "Zauberer"))
        self.AktivQuests.setText(_translate("DungeonWorldCharakter", "Quest"))
        self.belastungAktuell.setText(_translate("DungeonWorldCharakter", "0"))
        self.ruestungPunkte.setText(_translate("DungeonWorldCharakter", "0"))
        self.schadenWert.setText(_translate("DungeonWorldCharakter", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stats), _translate("DungeonWorldCharakter", "Stats"))
        self.muenzenText.setText(_translate("DungeonWorldCharakter", "Münzen"))
        self.edelsteineText.setText(_translate("DungeonWorldCharakter", "Edelsteine"))
        self.feldrationenText.setText(_translate("DungeonWorldCharakter", "Feldrationen"))
        self.gewichtText.setText(_translate("DungeonWorldCharakter", "Gewicht"))
        self.feldrationenGewicht.setText(_translate("DungeonWorldCharakter", "0"))
        self.abenteuerausruestungText.setText(_translate("DungeonWorldCharakter", "Abenteuerausrüstung"))
        self.heiltraenkeText.setText(_translate("DungeonWorldCharakter", "Heiltränke"))
        self.abenteuerausruestungGewicht.setText(_translate("DungeonWorldCharakter", "0"))
        self.gewichtText_2.setText(_translate("DungeonWorldCharakter", "Gewicht"))
        self.heiltraenkeGewicht.setText(_translate("DungeonWorldCharakter", "0"))
        self.gewichtText_3.setText(_translate("DungeonWorldCharakter", "Gewicht"))
        self.rucksackButton.setToolTip(_translate("DungeonWorldCharakter", "Öffnet den Rucksack, in welchem alle anderen Gegenstände angezeigt werden"))
        self.rucksackButton.setText(_translate("DungeonWorldCharakter", "Rucksack"))
        self.buendelpfeileText.setText(_translate("DungeonWorldCharakter", "Pfeile"))
        self.gewichtText_4.setText(_translate("DungeonWorldCharakter", "Gewicht"))
        self.buendelPfeileGewicht.setText(_translate("DungeonWorldCharakter", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inventory), _translate("DungeonWorldCharakter", "Ausrüstung"))
        self.geschick_2.setText(_translate("DungeonWorldCharakter", "Geschick"))
        self.weisheit_2.setText(_translate("DungeonWorldCharakter", "Weisheit"))
        self.schaden_2.setText(_translate("DungeonWorldCharakter", "Schaden"))
        self.staerke_2.setText(_translate("DungeonWorldCharakter", "Stärke"))
        self.charisma_2.setText(_translate("DungeonWorldCharakter", "Charisma"))
        self.ruestung_2.setText(_translate("DungeonWorldCharakter", "Rüstung"))
        self.intelligenz_2.setText(_translate("DungeonWorldCharakter", "Intelligenz"))
        self.konstitution_2.setText(_translate("DungeonWorldCharakter", "Konstitution"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.boni), _translate("DungeonWorldCharakter", "Boni"))
        self.actionLaden.setText(_translate("DungeonWorldCharakter", "Laden"))
        self.actionInventarloeschen.setText(_translate("DungeonWorldCharakter", "Inventar löschen"))

