import csv
import json

class operatorsPokemon:
    def extractPokemonCsv():
        routeCsv= ''
        listPokemon = []
        tuplePokemon= ()
        with open('appconfig.json') as config:
            routeCsv = json.load(config)
        
        with open(routeCsv['routeCsv']) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tuplePokemon = tuple(row)
                listPokemon.append(tuplePokemon)
        return listPokemon