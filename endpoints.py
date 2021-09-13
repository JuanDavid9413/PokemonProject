from flask import Flask, jsonify
from package.adminPackage import adminPackage


app = Flask(__name__)

@app.route('/getPokemon', methods=['GET'])
def getPokemon():
    try:
        return jsonify({'message': 'Ok', 'data': adminPackage.getPokemon(), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})

if __name__ == '__main__':
    app.run(debug=True, port = 4000)