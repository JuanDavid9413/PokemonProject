import sqlite3
from sqlite3.dbapi2 import Cursor


conn = sqlite3.connect('pokemonInfo.db', check_same_thread=False)
cursor = conn.cursor()

class packageAdminDB:
    def existTable():
        existTable = 0
        cursor.execute('''
        SELECT count(name) FROM sqlite_master WHERE type="table" AND name="Pokemons"
        ''')
        result = cursor.fetchone()
        for value in result:
            existTable = value
        return existTable
    
    def getPokemonsData(fieldName = None, search = None):
        query = 'SELECT * FROM Pokemons'
        if fieldName != None and search != None:
            query = 'SELECT * FROM Pokemons WHERE {0} LIKE "%{1}%"'.format(fieldName, search)

        cursor.execute(query)
        return cursor.fetchall()


    def createSchemma():
        cursor.execute('''
        CREATE TABLE Pokemons(
            id VARCHAR(100) NOT NULL,
            nombre VARCHAR(100) NOT NULL,
            typeOne VARCHAR(100) NOT NULL,
            typeTwo VARCHAR(100) NULL,
            total VARCHAR(100) NOT NULL,
            hp VARCHAR(100) NOT NULL,
            attack VARCHAR(100) NOT NULL,
            defense VARCHAR(100) NOT NULL,
            spAttack VARCHAR(100) NOT NULL,
            spDefense VARCHAR(100) NOT NULL,
            speed VARCHAR(100) NOT NULL,
            generation VARCHAR(100) NOT NULL,
            legendary VARCHAR(100) NOT NULL
        )
        ''')

        

    def createInfoDB(insertData):
        cursor.executemany('INSERT INTO Pokemons VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',insertData)
        cursor.execute('SELECT * FROM Pokemons')
        conn.commit()
        return cursor.fetchall()

    def getInfoDB():
        pass

    def deleteInfoBD():
        pass

    def updateInfoBD():
        pass