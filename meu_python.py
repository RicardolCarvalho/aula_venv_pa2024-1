from flask import Flask, request

app = Flask(__name__)

lista_alunos = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cadastra_aluno", methods=["POST"])
def cadastra_aluno_func():
    dic_aluno = request.json
    nome = dic_aluno.get('nome',"")
    if nome == '':
        resp = {"erro": "Nome não informado"}
        return resp, 400
    lista_alunos.append(dic_aluno)
    
    resp = {"mensagem": "Aluno Cadastrado",
            "aluno": dic_aluno}
    return resp, 201

@app.route("/lista_alunos", methods=['GET'])
def lista_alunos_func():
    resp = {'alunos': lista_alunos}
    return resp

if __name__ == "__main__":
    app.run(debug=True)