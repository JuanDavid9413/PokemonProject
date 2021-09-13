from package.packagePokemon.operatorsPokemon import operatorsPokemon
from package.packegeDB.packageAdminDB import packageAdminDB

class adminPackage:
    def getPokemon(field = None, value = None):
        if packageAdminDB.existTable() == 1:
            resultPokemon = packageAdminDB.getPokemonsData(field, value)
        else:
            packageAdminDB.createSchemma()
            resultPokemon = adminPackage.InsertDataBD(field, value)
        
        return resultPokemon
    

    def CreateTables():
        if packageAdminDB.existTable() != 1:
            packageAdminDB.createSchemma()
            return 'Los objetos de base de datos se crearon correctamente'
        else:
            return 'La tabla ya esta creada en la base de datos'
    

    def InsertDataBD():
        insertData = operatorsPokemon.extractPokemonCsv()
        del insertData[0]
        return packageAdminDB.createInfoDB(insertData)

        