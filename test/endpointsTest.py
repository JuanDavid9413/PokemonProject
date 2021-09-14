import sys
sys.path.append('../')
from package.adminPackage import adminPackage


class TestEndpoints():

    def getPokemon(self):
        """
            >>> adminPackage.getPokemon(field='name', value='Bulbasaur')
            [('1', 'Bulbasaur', 'Grass', 'Poison', '318', '45', '49', '49', '65', '65', '45', '1', 'False')]
        """

    def createSchema(self):
        """
            >>> adminPackage.CreateTables()
            'La tabla ya esta creada en la base de datos'
        """

    def InsertDataBD(self):
        """
            >>> adminPackage.InsertDataBD()
            [('1', 'Bulbasaur', 'Grass', 'Poison', '318', '45', '49', '49', '65', '65', '45', '1', 'False')]
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
