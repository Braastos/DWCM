import sys
import math
import os
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from MainGui import Ui_DungeonWorldCharakter
from InventoryEdit import Ui_itemEditor
from InventoryGui import Ui_inventoryManager
import tojson
import ctypes
from char import Stats,Inventory,Item, UpdateShit



myappid = 'braastos.dungeonworld.charaktermanager.first' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_DungeonWorldCharakter()

itemeditor = QDialog()
ui_editor = Ui_itemEditor()

inventory = None
ui_inventory = None


def kill_programm():
    save()
    sys.exit()


def deleteSave():
    os.remove("save.json")
    reloadUI()

def reloadUI():
    stats = Stats()
    data = tojson.loadfromsave()
    stats.load(data)
    inv = Inventory()
    print(data)
    inv.load(data)
    inituivalues(stats)
    initinvvalues(inv, data)

def updateui(stats):
    update = UpdateShit()
    ui.staerkeBonus.setText(update.calculateBonus(stats.staerke, stats.staerkeGM))
    ui.geschickBonus.setText(update.calculateBonus(stats.geschick, stats.geschickGM))
    ui.konstitutionBonus.setText(update.calculateBonus(stats.konstitution, stats.konstitutionGM))
    ui.intelligenzBonus.setText(update.calculateBonus(stats.intelligenz, stats.intelligenzGM))
    ui.weisheitBonus.setText(update.calculateBonus(stats.weisheit, stats.weisheitGM))
    ui.charismaBonus.setText(update.calculateBonus(stats.charisma, stats.charismaGM))
    ui.lebenMax.setText(str(stats.leben))
    ui.belastungMax.setText(str(stats.belastung))
    ui.schadenPunkte.setText(stats.schadenWuerfel)


def updateinv(inv,data):
    update = UpdateShit()
    ui.feldrationenGewicht.setText(str(update.calculateWeight(inv.feldrationen,5)))
    ui.abenteuerausruestungGewicht.setText(str(update.calculateWeight(inv.abenteuerausruestung,5)))
    ui.heiltraenkeGewicht.setText("0")
    ui.buendelPfeileGewicht.setText(str(update.calculateWeight(inv.pfeile,3)))
    ui.belastungAktuell.setText(str(update.updateWeight(data,ui)))
    newruestung = update.updateRuestung(data,ui)+ ui.ruestungBonus.value()
    newdamage = update.updateDamage(data,ui) + ui.schadenBonus.value()
    ui.ruestungPunkte.setText(str(newruestung))
    ui.schadenWert.setText(str(newdamage))


def inituivalues(stats):
    ui.Name.setText(stats.name)
    ui.klassenAuswahl.setCurrentText(stats.klasse)
    ui.stufePunkte.setValue(stats.stufe)
    ui.epPunkte.setValue(stats.ep)
    ui.staerkePunkte.setValue(stats.staerke)
    ui.staerkeBonusGM.setValue(stats.staerkeGM)
    ui.geschickPunkte.setValue(stats.geschick)
    ui.geschickBonusGM.setValue(stats.geschickGM)
    ui.konstitutionPunkte.setValue(stats.konstitution)
    ui.konstitutionBonusGM.setValue(stats.konstitutionGM)
    ui.intelligenzPunkte.setValue(stats.intelligenz)
    ui.intelligenzBonusGM.setValue(stats.intelligenzGM)
    ui.weisheitPunkte.setValue(stats.weisheit)
    ui.weisheitBonusGM.setValue(stats.weisheitGM)
    ui.charismaPunkte.setValue(stats.charisma)
    ui.charismaBonusGM.setValue(stats.charismaGM)
    ui.ruestungBonus.setValue(stats.ruestungGM)
    ui.lebenAktuell.setValue(stats.lebenAktuell)
    stats.update(ui)
    updateui(stats)

def initinvvalues(inv,data):
    ui.muenzen.setValue(inv.muenzen)
    ui.edelsteine.setValue(inv.edelsteine)
    ui.feldrationenMenge.setValue(inv.feldrationen)
    ui.abenteuerausruestungMenge.setValue(inv.abenteuerausruestung)
    ui.heiltraenkeMenge.setValue(inv.heiltraenke)
    ui.buendelPfeileMenge.setValue(inv.pfeile)
    updateinv(inv,data)



def save():
    data = tojson.loadfromsave()
    stats = Stats()
    inv = Inventory()
    stats.update(ui)
    data = stats.save(data,ui)
    updateui(stats)
    inv.update(ui)
    data = inv.save(data, ui)
    updateinv(inv, data)
    tojson.savetojson(data)


def loadItemStats():
    pass

def itemMinusOne():
    model = ui_inventory.inventoryView.model()
    selected = []
    data = tojson.loadfromsave()
    indexes = ui_inventory.inventoryView.selectionModel().selectedRows()
    for i in sorted(indexes):
        row = i.row()
        print(row)
        index = model.index(row, 0)
        # We suppose data are strings
        selected.append(model.data(index))
        strselected = "".join(selected)
        print(selected)
        for element in data["Inventory"]:
            if element == strselected:
                menge = data["Inventory"][strselected]["menge"]
                newMenge = int(menge)-1
                data["Inventory"][strselected].update({"menge": newMenge})
                gewicht = data["Inventory"][strselected]["gewicht"]
                newGewicht = math.ceil(gewicht/menge*newMenge)
                if newMenge <= 0:
                    del data["Inventory"][strselected]
                else:
                    data["Inventory"][strselected].update({"menge":newMenge})
                    data["Inventory"][strselected].update({"gewicht": newGewicht})
                tojson.savetojson(data)
                updateListView()
                inv = Inventory()
                inv.update(ui)
                data = inv.save(data, ui)
                updateinv(inv, data)
                break


def itemMinusFive():
    model = ui_inventory.inventoryView.model()
    selected = []
    data = tojson.loadfromsave()
    indexes = ui_inventory.inventoryView.selectionModel().selectedRows()
    for i in sorted(indexes):
        row = i.row()
        print(row)
        index = model.index(row, 0)
        # We suppose data are strings
        selected.append(model.data(index))
        strselected = "".join(selected)
        print(selected)
        for element in data["Inventory"]:
            if element == strselected:
                menge = data["Inventory"][strselected]["menge"]
                newMenge = int(menge)-5
                data["Inventory"][strselected].update({"menge": newMenge})
                gewicht = data["Inventory"][strselected]["gewicht"]
                newGewicht = math.ceil(gewicht/menge*newMenge)
                if newMenge <= 0:
                    del data["Inventory"][strselected]
                else:
                    data["Inventory"][strselected].update({"menge":newMenge})
                    data["Inventory"][strselected].update({"gewicht": newGewicht})
                tojson.savetojson(data)
                updateListView()
                inv = Inventory()
                inv.update(ui)
                data = inv.save(data, ui)
                updateinv(inv, data)
                break

def itemPlusOne():
    model = ui_inventory.inventoryView.model()
    selected = []
    data = tojson.loadfromsave()
    indexes = ui_inventory.inventoryView.selectionModel().selectedRows()
    for i in sorted(indexes):
        row = i.row()
        print(row)
        index = model.index(row, 0)
        # We suppose data are strings
        selected.append(model.data(index))
        strselected = "".join(selected)
        print(selected)
        for element in data["Inventory"]:
            if element == strselected:
                menge = data["Inventory"][strselected]["menge"]
                newMenge = int(menge)+1
                data["Inventory"][strselected].update({"menge": newMenge})
                gewicht = data["Inventory"][strselected]["gewicht"]
                newGewicht = math.ceil(gewicht/menge*newMenge)
                if newMenge <= 0:
                    del data["Inventory"][strselected]
                else:
                    data["Inventory"][strselected].update({"menge":newMenge})
                    data["Inventory"][strselected].update({"gewicht": newGewicht})
                tojson.savetojson(data)
                updateListView()
                inv = Inventory()
                inv.update(ui)
                data = inv.save(data, ui)
                updateinv(inv, data)
                break


def itemPlusFive():
    model = ui_inventory.inventoryView.model()
    selected = []
    data = tojson.loadfromsave()
    indexes = ui_inventory.inventoryView.selectionModel().selectedRows()
    for i in sorted(indexes):
        row = i.row()
        print(row)
        index = model.index(row, 0)
        # We suppose data are strings
        selected.append(model.data(index))
        strselected = "".join(selected)
        print(selected)
        for element in data["Inventory"]:
            if element == strselected:
                menge = data["Inventory"][strselected]["menge"]
                newMenge = int(menge)+5
                data["Inventory"][strselected].update({"menge": newMenge})
                gewicht = data["Inventory"][strselected]["gewicht"]
                newGewicht = math.ceil(gewicht/menge*newMenge)
                if newMenge <= 0:
                    del data["Inventory"][strselected]
                else:
                    data["Inventory"][strselected].update({"menge":newMenge})
                    data["Inventory"][strselected].update({"gewicht": newGewicht})
                tojson.savetojson(data)
                updateListView()
                inv = Inventory()
                inv.update(ui)
                data = inv.save(data, ui)
                updateinv(inv, data)
                break







def saveItem():
    x = Item()
    data = tojson.loadfromsave()
    global ui_editor
    x.create(ui_editor)
    data = x.save(data)
    tojson.savetojson(data)
    closeEditor()
    updateListView()

def updateListView():
    global ui_inventory
    data = tojson.loadfromsave()
    model = QStandardItemModel()
    if model.rowCount() is not 0:
        model.removeRows(0,model.rowCount())
        ui_inventory.inventoryView.setModel(model)
    counter = 0
    for inv in data["Inventory"]:


        if inv == "muenzen":
            pass
        elif inv == "edelsteine":
            pass
        elif inv == "feldrationen":
            pass
        elif inv == "abenteuerausruestung":
            pass
        elif inv == "heiltraenke":
            pass
        elif inv == "pfeile":
            pass
        else:
            item = None
            gegenstand = None
            l = []
            l.append("Menge: ")
            l.append(str(data["Inventory"][inv]["menge"]))
            l.append(" Gewicht: ")
            l.append(str(data["Inventory"][inv]["gewicht"]))
            l.append(" ")

            if data["Inventory"][inv]["staerke"] is not 0:
                l.append("Stärke: ")
                if data["Inventory"][inv]["staerke"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["staerke"]))
                l.append(" ")
            if data["Inventory"][inv]["geschick"] is not 0:
                l.append("Geschick: ")
                if data["Inventory"][inv]["geschick"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["geschick"]))
                l.append(" ")
            if data["Inventory"][inv]["konstitution"] is not 0:
                l.append("Konstitution: ")
                if data["Inventory"][inv]["konstitution"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["konstitution"]))
                l.append(" ")
            if data["Inventory"][inv]["intelligenz"] is not 0:
                l.append("Intelligenz: ")
                if data["Inventory"][inv]["intelligenz"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["intelligenz"]))
                l.append(" ")
            if data["Inventory"][inv]["weisheit"] is not 0:
                l.append("Weisheit: ")
                if data["Inventory"][inv]["weisheit"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["weisheit"]))
                l.append(" ")
            if data["Inventory"][inv]["charisma"] is not 0:
                l.append("Charisma: ")
                if data["Inventory"][inv]["charisma"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["charisma"]))
                l.append(" ")
            if data["Inventory"][inv]["ruestung"] is not 0:
                l.append("Rüstung: ")
                if data["Inventory"][inv]["ruestung"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["ruestung"]))
                l.append(" ")
            if data["Inventory"][inv]["schaden"] is not 0:
                l.append("Schaden: ")
                if data["Inventory"][inv]["schaden"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["schaden"]))
                l.append(" ")
            if data["Inventory"][inv]["leben"] is not 0:
                l.append("Leben: ")
                if data["Inventory"][inv]["leben"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["leben"]))
                l.append(" ")
            if data["Inventory"][inv]["belastung"] is not 0:
                l.append("Belastung: ")
                if data["Inventory"][inv]["belastung"] > 0:
                    l.append("+")
                l.append(str(data["Inventory"][inv]["belastung"]))
                l.append(" ")
            gegenstand = "".join(l)
            name = QStandardItem(inv)
            item = QStandardItem(gegenstand)
            beschreibung = QStandardItem(str(data["Inventory"][inv]["beschreibung"]))
            itemList = (name,beschreibung,item)
            model.insertRow(counter,itemList)
            counter = counter + 1
            model.setHorizontalHeaderLabels(["Name","Beschreibung","Stats"])
    ui_inventory.inventoryView.setModel(model)
    ui_inventory.inventoryView.resizeColumnToContents(0)
    ui_inventory.inventoryView.resizeColumnToContents(1)
    ui_inventory.inventoryView.resizeColumnToContents(2)

def openrucksack():
    global inventory
    global ui_inventory
    inventory = QDialog()
    ui_inventory = Ui_inventoryManager()#extended()
    ui_inventory.setupUi(inventory)
    inventory.show()
    updateListView()
    ui_inventory.erstellenButton.clicked.connect(openEditor)
    ui_inventory.minusOneButton.clicked.connect(itemMinusOne)
    ui_inventory.minusFiveButton.clicked.connect(itemMinusFive)
    ui_inventory.plusOneButton.clicked.connect(itemPlusOne)
    ui_inventory.plusFiveButton.clicked.connect(itemPlusFive)




def openEditor():
    global itemeditor
    global ui_editor
    itemeditor = QDialog()
    ui_editor = Ui_itemEditor()
    ui_editor.setupUi(itemeditor)
    ui_editor.speichernButton.clicked.connect(saveItem)
    ui_editor.abbrechenButton.clicked.connect(closeEditor)
    itemeditor.show()

def closeEditor():
    global itemeditor
    global ui_editor
    itemeditor.close()
    itemeditor = None
    ui_editor = None
    print("Closed")



def StartUpdate():
    ui.staerkePunkte.valueChanged.connect(save)
    ui.geschickPunkte.valueChanged.connect(save)
    ui.konstitutionPunkte.valueChanged.connect(save)
    ui.intelligenzPunkte.valueChanged.connect(save)
    ui.weisheitPunkte.valueChanged.connect(save)
    ui.charismaPunkte.valueChanged.connect(save)
    ui.staerkeBonusGM.valueChanged.connect(save)
    ui.geschickBonusGM.valueChanged.connect(save)
    ui.konstitutionBonusGM.valueChanged.connect(save)
    ui.intelligenzBonusGM.valueChanged.connect(save)
    ui.weisheitBonusGM.valueChanged.connect(save)
    ui.charismaBonusGM.valueChanged.connect(save)
    ui.klassenAuswahl.activated.connect(save)
    ui.lebenAktuell.valueChanged.connect(save)
    ui.muenzen.valueChanged.connect(save)
    ui.edelsteine.valueChanged.connect(save)
    ui.feldrationenMenge.valueChanged.connect(save)
    ui.abenteuerausruestungMenge.valueChanged.connect(save)
    ui.heiltraenkeMenge.valueChanged.connect(save)
    ui.buendelPfeileMenge.valueChanged.connect(save)
    ui.rucksackButton.clicked.connect(openrucksack)
    ui.ruestungBonus.valueChanged.connect(save)
    ui.schadenBonus.valueChanged.connect(save)
    ui.actionCharakter_loeschen.triggered.connect(deleteSave)
    ui.actionProgramm_beenden.triggered.connect(kill_programm)



def main():
    ui.setupUi(window)
    window.show()
    reloadUI()
    StartUpdate()
    sys.exit(app.exec_())






if __name__  == "__main__":
    main()


