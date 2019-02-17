import sqlite3


dbfile = 'Charakter.db'


def dbinsertChar (input):
    try:

        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Charakter VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', input)
        conn.commit()
        conn.close()
    except all as e:
        print(e)


def dbsearch():
    pass

def dbinsertInv(input):
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Inventory VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', input)
    conn.commit()
    conn.close()

def dbread(table):
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    for row in cursor.execute('SELECT * FROM ?', table):
        conn.close()
        return row

def dbdeleteChar(delete):
    try:
        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Charakter WHERE Name = ?', delete)
        cursor.execute('DELETE FROM Inventory')
        conn.commit()
        conn.close()

    except:
        print("An Error Occured")


def dbdeleteItem(delete):
    try:
        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Inventory WHERE ItemName = ?', delete)
        conn.commit()
        conn.close()

    except:
        print("An Error Occured")
