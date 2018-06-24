import math

class UpdateShit:
    schadenWuerfel = "Error"
    baselife = -20
    basebelastung = -20
    bonus = "Error"

    def klassenSpecs(self,klasse):
        if klasse == "Barbar":
            self.schadenWuerfel = "W10"
            self.baselife = 8
            self.basebelastung = 8
        if klasse == "Barde":
            self.schadenWuerfel = "W6"
            self.baselife = 6
            self.basebelastung = 9
        if klasse == "Druide":
            self.schadenWuerfel = "W6"
            self.baselife = 6
            self.basebelastung = 6
        if klasse == "Kleriker":
            self.schadenWuerfel = "W6"
            self.baselife = 8
            self.basebelastung = 8
        if klasse == "Kämpfer":
            self.schadenWuerfel = "W10"
            self.baselife = 10
            self.basebelastung = 12
        if klasse == "Paladin":
            self.schadenWuerfel = "W10"
            self.baselife = 10
            self.basebelastung = 12
        if klasse == "Waldläufer":
            self.schadenWuerfel = "W8"
            self.baselife = 8
            self.basebelastung = 11
        if klasse == "Schurke":
            self.schadenWuerfel = "W8"
            self.baselife = 6
            self.basebelastung = 9
        if klasse == "Zauberer":
            self.schadenWuerfel = "W4"
            self.baselife = 4
            self.basebelastung = 7

        returnvalue = (self.schadenWuerfel, self.baselife, self.basebelastung)
        return returnvalue

    def calculateBonus(self,stats,GMBonus):

        if stats >= 1 and stats <= 3:
            bonus = -3
        elif stats >= 4 and stats <= 5:
            bonus = -2
        elif stats >= 6 and stats <= 8:
            bonus = -1
        elif stats >= 9 and stats <= 12:
            bonus = 0
        elif stats >= 13 and stats <= 15:
            bonus = 1
        elif stats >= 16 and stats <= 17:
            bonus = 2
        elif stats == 18:
            bonus = 3
        else:
            bonus = 0

        bonus = GMBonus + bonus

        if bonus == 0:
            strbonus = ("-")
        elif bonus > 0:
            strbonus = ('+{}'.format(bonus))
        elif bonus < 0:
            strbonus = ('{}'.format(bonus))

        return strbonus

    def calculateWeight(self,stacksize,maxstacksize):
        gewicht = int(math.ceil(stacksize / maxstacksize))
        return gewicht

    def updateWeight(self,data,ui):
        gewicht = 0
        if data is not None:
            if "Inventory" in data:
                #for i in range(len(data["Inventory"])):
                for item in data["Inventory"]:
                    tocheck = data["Inventory"][item]
                    if "dict" == type(tocheck).__name__:
                        if "gewicht" in tocheck:
                            gewicht = int(data["Inventory"][item]["gewicht"])+gewicht
            gewicht = int(ui.feldrationenGewicht.text()) + int(ui.abenteuerausruestungGewicht.text()) + int(ui.heiltraenkeGewicht.text()) + int(ui.buendelPfeileGewicht.text()) + gewicht
            return gewicht

    def updateRuestung(self,data,ui):
        ruestung = 0
        if data is not None:
            if "Inventory" in data:
                # for i in range(len(data["Inventory"])):
                for item in data["Inventory"]:
                    tocheck = data["Inventory"][item]
                    if "dict" == type(tocheck).__name__:
                        if "ruestung" in tocheck:
                            ruestung = int(data["Inventory"][item]["ruestung"]) + ruestung
            return ruestung






class Stats:
    name = ""
    klasse = "Barbar"
    stufe = 1
    ep = 0
    staerke = 0
    staerkeGM = 0
    geschick = 0
    geschickGM = 0
    konstitution = 0
    konstitutionGM = 0
    intelligenz = 0
    intelligenzGM = 0
    weisheit = 0
    weisheitGM = 0
    charisma = 0
    charismaGM = 0
    ruestungGM = 0
    schaden = 0
    schadenGM = 0
    schadenWuerfel = "Error"
    leben = 0
    lebenAktuell = 0
    belastung = 0
    belastungAktuell = 0

    def load(self,data):
        try:
            self.name = data["Name"]
        except:
            print("Failed to load Name")
        try:
            self.klasse = data["klassenAuswahl"]
        except:
            print("Failed to load Class")
        try:
            self.stufe = data["stufePunkte"]
        except:
            print("Failed to load Level")
        try:
            self.ep = data["epPunkte"]
        except:
            print("Failed to load EP")
        try:
            self.staerke = data["staerkePunkte"]
        except:
            print("Failed to load Strength")
        try:
            self.staerkeGM = data["staerkeBonusGM"]
        except:
            print("Failed to load GM Bonus Strength")
        try:
            self.geschick = data["geschickPunkte"]
        except:
            print("Failed to load Dexterity")
        try:
            self.geschickGM = data["geschickBonusGM"]
        except:
            print("Failed to load GM Bonus Dexterity")
        try:
            self.konstitution = data["konstitutionPunkte"]
        except:
            print("Failed to load Constitution")
        try:
            self.konstitutionGM = data["konstitutionBonusGM"]
        except:
            print("Failed to load GM Bonus Constitution")
        try:
            self.intelligenz = data["intelligenzPunkte"]
        except:
            print("Failed to load Intelligence")
        try:
            self.intelligenzGM = data["intelligenzBonusGM"]
        except:
            print("Failed to load GM Bonus Intelligence")
        try:
            self.weisheit = data["weisheitPunkte"]
        except:
            print("Failed to load Wisdom")
        try:
            self.weisheitGM = data["weisheitBonusGM"]
        except:
            print("Failed to load GM Bonus Wisdom")
        try:
            self.charisma = data["charismaPunkte"]
        except:
            print("Failed to load Charisma")
        try:
            self.charismaGM = data["charismaBonusGM"]
        except:
            print("Failed to load GM Bonus Charisma")
        try:
            self.ruestungGM = data["ruestungBonus"]
        except:
            print("Failed to load GM Bonus Defence")
        try:
            self.lebenAktuell = data["lebenAktuell"]
        except:
            print("Failed to load current live")
        try:
            self.schadenGM = data["schadenGM"]
        except:
            print("Failed to load current GM Bonus Damage")



    def save(self,data,ui):
        if data is None:
            data = {ui.klassenAuswahl.objectName(): self.klasse,
                     ui.Name.objectName(): self.name,
                     ui.stufePunkte.objectName(): self.stufe,
                     ui.epPunkte.objectName(): self.ep,
                     ui.staerkePunkte.objectName(): self.staerke,
                     ui.staerkeBonusGM.objectName(): self.staerkeGM,
                     ui.geschickPunkte.objectName(): self.geschick,
                     ui.geschickBonusGM.objectName(): self.geschickGM,
                     ui.konstitutionPunkte.objectName(): self.konstitution,
                     ui.konstitutionBonusGM.objectName(): self.konstitutionGM,
                     ui.intelligenzPunkte.objectName(): self.intelligenz,
                     ui.intelligenzBonusGM.objectName(): self.intelligenzGM,
                     ui.weisheitPunkte.objectName(): self.weisheit,
                     ui.weisheitBonusGM.objectName(): self.weisheitGM,
                     ui.charismaPunkte.objectName(): self.charisma,
                     ui.charismaBonusGM.objectName(): self.charismaGM,
                     ui.ruestungBonus.objectName(): self.ruestungGM,
                     ui.lebenAktuell.objectName(): self.lebenAktuell,
                     }
        else:
            data.update({ui.klassenAuswahl.objectName(): self.klasse,
                         ui.Name.objectName(): self.name,
                         ui.stufePunkte.objectName(): self.stufe,
                         ui.epPunkte.objectName(): self.ep,
                         ui.staerkePunkte.objectName(): self.staerke,
                         ui.staerkeBonusGM.objectName(): self.staerkeGM,
                         ui.geschickPunkte.objectName(): self.geschick,
                         ui.geschickBonusGM.objectName(): self.geschickGM,
                         ui.konstitutionPunkte.objectName(): self.konstitution,
                         ui.konstitutionBonusGM.objectName(): self.konstitutionGM,
                         ui.intelligenzPunkte.objectName(): self.intelligenz,
                         ui.intelligenzBonusGM.objectName(): self.intelligenzGM,
                         ui.weisheitPunkte.objectName(): self.weisheit,
                         ui.weisheitBonusGM.objectName(): self.weisheitGM,
                         ui.charismaPunkte.objectName(): self.charisma,
                         ui.charismaBonusGM.objectName(): self.charismaGM,
                         ui.ruestungBonus.objectName(): self.ruestungGM,
                         ui.lebenAktuell.objectName(): self.lebenAktuell,
                         })
        return data

    def update(self,ui):
        self.klasse = ui.klassenAuswahl.currentText()
        self.name = ui.Name.toPlainText()
        self.stufe = ui.stufePunkte.value()
        self.ep = ui.epPunkte.value()
        self.staerke = ui.staerkePunkte.value()
        self.staerkeGM = ui.staerkeBonusGM.value()
        self.geschick = ui.geschickPunkte.value()
        self.geschickGM = ui.geschickBonusGM.value()
        self.konstitution = ui.konstitutionPunkte.value()
        self.konstitutionGM = ui.konstitutionBonusGM.value()
        self.intelligenz = ui.intelligenzPunkte.value()
        self.intelligenzGM = ui.intelligenzBonusGM.value()
        self.weisheit = ui.weisheitPunkte.value()
        self.weisheitGM = ui.weisheitBonusGM.value()
        self.charisma = ui.charismaPunkte.value()
        self.charismaGM = ui.charismaBonusGM.value()
        self.lebenAktuell = ui.lebenAktuell.value()
        update = UpdateShit()
        values = update.klassenSpecs(self.klasse)
        self.schadenWuerfel = values[0]
        self.leben = values[1] + self.konstitution
        self.belastung = values[2] + self.staerke
        self.ruestungGM = ui.ruestungBonus.value()
        self.belastungAktuell = 0





class Inventory:
    muenzen = 0
    edelsteine = 0
    feldrationen = 0
    abenteuerausruestung = 0
    heiltraenke = 0
    pfeile = 0

    def load(self,data):
        try:
            print(data["Inventory"]["muenzen"])
            self.muenzen = data["Inventory"]["muenzen"]
        except:
            print("Failed to load some Items")
        try:
            self.edelsteine =  data["Inventory"]["edelsteine"]
        except:
            print("Failed to load some Items")
        try:
            self.feldrationen = data["Inventory"]["feldrationen"]
        except:
            print("Failed to load some Items")
        try:
            self.abenteuerausruestung = data["Inventory"]["abenteuerausruestung"]
        except:
            print("Failed to load some Items")
        try:
            self.heiltraenke =  data["Inventory"]["heiltraenke"]
        except:
            print("Failed to load some Items")
        try:
            self.pfeile = data["Inventory"]["pfeile"]
        except:
            print("Failed to load some Items")

    def save(self,data,ui):
        if "Inventory" in data:
            data["Inventory"].update({
                "muenzen":self.muenzen,
                "edelsteine":self.edelsteine,
                "feldrationen":self.feldrationen,
                "abenteuerausruestung":self.abenteuerausruestung,
                "heiltraenke":self.heiltraenke,
                "pfeile":self.pfeile
            })
        else:
            data.update({"Inventory":{
                "muenzen": self.muenzen,
                "edelsteine": self.edelsteine,
                "feldrationen": self.feldrationen,
                "abenteuerausruestung": self.abenteuerausruestung,
                "heiltraenke": self.heiltraenke,
                "pfeile": self.pfeile
            }})
        return data

    def update(self,ui):
        self.muenzen = ui.muenzen.value()
        self.edelsteine = ui.edelsteine.value()
        self.feldrationen = ui.feldrationenMenge.value()
        self.abenteuerausruestung = ui.abenteuerausruestungMenge.value()
        self.heiltraenke = ui.heiltraenkeMenge.value()
        self.pfeile = ui.buendelPfeileMenge.value()



class Item:
    name = ""
    menge = 0
    gewicht = 0
    beschreibung = "Ein Platzhalteritem, dieses Item hat keine Auswirkungen auf das Spiel"
    staerke = 0
    geschick = 0
    konstitution = 0
    intelligenz = 0
    weisheit = 0
    charisma = 0
    ruestung = 0
    schaden = 0
    leben = 0
    belastung = 0

    def create(self, ui):
        self.name = ui.gegenstand.text()
        self.menge = ui.menge.value()
        self.gewicht = ui.gewicht.value()
        self.beschreibung = ui.beschreibung.text()
        self.staerke = ui.staerke.value()
        self.geschick = ui.geschick.value()
        self.konstitution = ui.konstitution.value()
        self.intelligenz = ui.intelligenz.value()
        self.weisheit = ui.weisheit.value()
        self.charisma = ui.charisma.value()
        self.ruestung = ui.ruestung.value()
        self.schaden = ui.schaden.value()
        self.leben = ui.leben.value()
        self.belastung = ui.belastung.value()

    def save(self,data):
        if "Inventory" in data:
            if self.name != "":
                item = ({self.name:{"menge": self.menge, "gewicht": self.gewicht, "beschreibung": self.beschreibung}})

                stat = {"staerke": self.staerke}
                item[self.name].update(stat)

                stat = {"geschick": self.geschick}
                item[self.name].update(stat)

                stat = {"konstitution": self.konstitution}
                item[self.name].update(stat)

                stat = {"intelligenz": self.intelligenz}
                item[self.name].update(stat)

                stat = {"weisheit": self.weisheit}
                item[self.name].update(stat)

                stat = {"charisma": self.charisma}
                item[self.name].update(stat)

                stat = {"ruestung": self.ruestung}
                item[self.name].update(stat)

                stat = {"schaden": self.schaden}
                item[self.name].update(stat)

                stat = {"leben": self.leben}
                item[self.name].update(stat)

                stat = {"belastung": self.belastung}
                item[self.name].update(stat)

                data["Inventory"].update(item)
                return data
        else:
            data.update({"Inventory":self.name})
            if self.name != "":
                item = ({self.name: {"menge": self.menge, "gewicht": self.gewicht, "beschreibung": self.beschreibung}})

                stat = {"staerke": self.staerke}
                item[self.name].update(stat)

                stat = {"geschick": self.geschick}
                item[self.name].update(stat)

                stat = {"konstitution": self.konstitution}
                item[self.name].update(stat)

                stat = {"intelligenz": self.intelligenz}
                item[self.name].update(stat)

                stat = {"weisheit": self.weisheit}
                item[self.name].update(stat)

                stat = {"charisma": self.charisma}
                item[self.name].update(stat)

                stat = {"ruestung": self.ruestung}
                item[self.name].update(stat)

                stat = {"schaden": self.schaden}
                item[self.name].update(stat)

                stat = {"leben": self.leben}
                item[self.name].update(stat)

                stat = {"belastung": self.belastung}
                item[self.name].update(stat)

                data["Inventory"].update(item)
                return data


