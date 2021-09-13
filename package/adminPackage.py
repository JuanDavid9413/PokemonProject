from package.packagePokemon.operatorsPokemon import operatorsPokemon
from package.packegeDB.packageAdminDB import packageAdminDB

class adminPackage:
    def getPokemon():
        existTable = packageAdminDB.existTable()
        if existTable == 1:
            resultPokemon = adminPackage.validateInformationBD()
        else:
            packageAdminDB.createSchemma()
            resultPokemon = adminPackage.validateInformationBD()
        
        return resultPokemon
            

    def validateInformationBD():
        pokemonData = packageAdminDB.getPokemonsData()
        if len(pokemonData) == 0:
            insertData = operatorsPokemon.extractPokemonCsv()
            del insertData[0] 
            return packageAdminDB.createInfoDB(insertData)
        else:
            return pokemonData