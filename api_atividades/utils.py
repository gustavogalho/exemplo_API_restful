from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome="Galho", idade=25)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Galho").first()
    print(pessoa.idade)


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Galho").first()
    pessoa.idade = 24
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Galho").first()
    pessoa.delete()


if __name__ == "__main__":
    # insere_pessoas()
    consulta_pessoas()
    # exclui_pessoa()
    # altera_pessoas()
