from flask import Flask, json, jsonify, request

app = Flask(__name__)


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
# devolve, altera e deleta um desenvolvedor pelo ID


@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {
                "status": "erro",
                "mensagem": "Desenvolvedor de ID {} não existe".format(id)
            }
        except Exception:
            response = {
                "status": "erro",
                "mensagem": "Procure um administrador"
            }
        return jsonify(response)

    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({
            "status": "Sucesso",
            "mensagem": "registro excluido"
        })

# lista todos os desenvolvedores e inclui um novo desenvolvedor


@app.route("/dev/", methods=["GET", "POST"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])


    elif request.method == "GET":
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)
