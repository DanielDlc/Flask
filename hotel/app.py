from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'alpha hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },

    {
        'hotel_id': 'bravo',
        'nome': 'bravo hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
    },

    {
        'hotel_id': 'charlie',
        'nome': 'charlie hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'São Paulo'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
api.add_resource(Hoteis, '/hoteis')    


if __name__ == '__main__':
    app.run(debug=True)