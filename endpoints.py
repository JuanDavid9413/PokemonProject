from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from
import json
from package.adminPackage import adminPackage


app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

swagger = Swagger(app, config=swagger_config)

@app.route('/Pokemon', methods=['GET'])
@swag_from('swagger_config.yml')
def getPokemon():
    try:
        field = request.args.get('field')
        value = request.args.get('value')        
        return jsonify({'message': 'Ok', 'data': adminPackage.getPokemon(field, value), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})

@app.route('/createSchema', methods=['GET'])
@swag_from('swagger_config.yml')
def createSchema():
    try:
        return jsonify({'message': 'Ok', 'data': adminPackage.CreateTables(), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})

@app.route('/createInformation', methods=['POST'])
@swag_from('swagger_config.yml')
def createInformationDB():
    try:
        return jsonify({'message': 'Ok', 'data': adminPackage.InsertDataBD(), 'status': '200'})
    except:
        return jsonify({'message': 'Internal Server Error', 'data': None, 'status': '500'})


if __name__ == '__main__':
    app.run(debug=True, port = 4000)