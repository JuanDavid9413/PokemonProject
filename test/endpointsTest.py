import unittest
from package.adminPackage import adminPackage


class TestEndpoints(unittest.TestCase):
    def getPokemon(self):
        self.assertEqual(adminPackage.getPokemon(), [()])

    def createSchema(self):
        self.assertNotEqual(adminPackage.CreateTables(), 'La tabla ya esta creada en la base de datos')

    def createInformationDB(self):
        self.assertEqual(adminPackage.InsertDataBD(), [()])


if __name__ == '__main__':
    unittest.main()
