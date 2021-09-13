from flask import json, request
from flask_restful import Resource

lista_habilidades = [
    "Python",
    "Java",
    "Flask",
    "PHP"
]


class ListaHabilidades(Resource):
    def get(self):
        try:
            response = lista_habilidades
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response

    def post(self):
        try:
            dados = json.loads(request.data)
            lista_habilidades.append(dados["habilidade"])
            response = {
                "status": "Sucesso",
                "mensagem": "Habilidade adicionada a lista"
            }
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response


class Habilidade(Resource):
    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            response = {
                "status": "Sucesso",
                "mensagem": "Habilidade excluida"
            }
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            lista_habilidades[id] = dados["habilidade"]
            response = {
                "status": "Sucesso",
                "mensagem": "Habilidade alterada"
            }
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response
