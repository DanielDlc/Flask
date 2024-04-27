from flask_restful import Resource, reqparse
from flask import jsonify


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
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found!'}, 404 # Não encontrado

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome', type=str, required=True)
        argumentos.add_argument('estrelas', type=float, required=True)
        argumentos.add_argument('diaria', type=float, required=True)
        argumentos.add_argument('cidade', type=str, required=True)

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': str(dados['estrelas']),
            'diaria': str(dados['diaria']),
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)

        return {'hotel': novo_hotel}, 200


    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass