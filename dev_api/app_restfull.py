from flask import Flask, request, json
from flask_restful import Resource, Api
from habilidades import ListaHabilidades, Habilidade

desenvolvedores = [
    {
        "id": "0",
        "nome": "Gustavo",
        "habilidades": ["Python", "Flask"]
    },
    {
        "id": "1",
        "nome": "Galho",
        "habilidades": ["Python", "Django"]
    }
]

app = Flask(__name__)
api = Api(app)

# devolve, altera e deleta um desenvolvedor pelo ID


class Desenvolvedores(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {
                "status": "erro",
                "mensagem": f"Desenvolvedor de ID '{id}' não existe"
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
            desenvolvedores[id] = dados
            response = {
                "status": "Sucesso",
                "mensagem": "registro alterado"
            }
        except Exception as err:
            response = {
                "status": "Erro",
                "mensagem": f"{err}"
            }
        return response

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            response = {
                "status": "Sucesso",
                "mensagem": "registro excluido"
            }
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response


# Lista todos as tarefas e permite criar uma nova


class ListaDesenvolvedores(Resource):
    def get(self):
        try:
            response = desenvolvedores
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response

    def post(self):
        try:
            dados = json.loads(request.data)
            pos = len(desenvolvedores)
            dados["id"] = pos
            desenvolvedores.append(dados)
            response = desenvolvedores[pos]
        except Exception as err:
            response = {
                "status": "erro",
                "mensagem": f"{err}"
            }
        return response


api.add_resource(Desenvolvedores, "/dev/<int:id>")
api.add_resource(ListaDesenvolvedores, "/dev")

api.add_resource(ListaHabilidades, "/habilidades")
api.add_resource(Habilidade, "/habilidades/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
