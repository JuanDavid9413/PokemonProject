import csv

class operatorsPokemon:
    def extractPokemonCsv():
        listPokemon = [];
        tuplePokemon= ()
        with open('D:\Pruebas\AutoLab\package\packagePokemon\pokemon.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tuplePokemon = tuple(row)
                listPokemon.append(tuplePokemon)
        return listPokemon