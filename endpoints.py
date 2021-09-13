from flask import Flask, jsonify, request
import json
from package.adminPackage import adminPackage


app = Flask(__name__)

@app.route('/Pokemon', methods=['GET'])
def getPokemon():
    try:
        field = request.args.get('field')
        value = request.args.get('value')
        return jsonify({'message': 'Ok', 'data': adminPackage.getPokemon(field, value), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})

@app.route('/createSchema', methods=['GET'])
def createSchema():
    try:
        return jsonify({'message': 'Ok', 'data': adminPackage.CreateTables(), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})

@app.route('/createInformation', methods=['GET'])
def createInformationDB():
    try:
        return jsonify({'message': 'Ok', 'data': adminPackage.InsertDataBD(), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})


if __name__ == '__main__':
    app.run(debug=True, port = 4000)