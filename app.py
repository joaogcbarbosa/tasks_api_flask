from flask import Flask, jsonify, request
from json import loads

app = Flask(__name__)

tasks = [
    {'id': 0,
    'responsavel': 'João Gabriel Barbosa',
    'tarefa': 'Desenvolver API',
    'status': 'Em andamento'},

    {'id': 1,
    'responsavel': 'José Miguel Pires',
    'tarefa': 'Desenvolver App Mobile',
    'status': 'Pausado'},

    {'id': 2,
    'responsavel': 'Hugo Soares',
    'tarefa': 'Desenvolver Página',
    'status': 'Feito'}
]


@app.route("/", methods=['GET'])
def home():
    return ('<h1>Página Inicial</h1>'
           '<h2><a href="http://127.0.0.1:5000/todas-tarefas/">Todas Tarefas</a><br></h2>'
           '<h3>Para pesquisar(GET) ou excluir(DELETE) tarefa por ID: http://127.0.0.1:5000/tarefa/"id"/</h3>'
           '<h3>Para inserir(POST) tarefa: http://127.0.0.1:5000/incluir-tarefa/</h3>'
           '<h3>Para alterar(PUT) somente o status: http://127.0.0.1:5000/alterar-status/"id"/</h3>')


@app.route("/todas-tarefas/", methods=['GET'])
def todas_tarefas():
    return jsonify(tasks)


@app.route("/incluir-tarefa/", methods=['POST'])
def incluir_tarefa():
    dados = loads(request.data)
    posicao = len(tasks)
    dados['id'] = posicao
    tasks.append(dados)
    return jsonify({'status': 'Sucesso!',
                    'mensagem': 'Registro inserido.'})


@app.route("/alterar-status/<int:id>/", methods=['PUT'])
def alterar_status(id):
    dados = loads(request.data)
    tasks[id]['status'] = dados['status']
    return jsonify({'status': 'Sucesso!',
                    'mensagem': 'Status alterado.'})


@app.route("/tarefa/<int:id>/", methods=['GET', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            dados = tasks[id]
        except IndexError:
            mensagem = f'NÃO HÁ TAREFA VINCULADA AO ID {id}'
            dados = {'status': 'ERRO!', 
                    'mensagem': mensagem}
        except Exception():
            mensagem = f'ERRO DESCONHECIDO. RECORRER AO DESENVOLVEDOR'
            dados = {'status': 'ERRO!',
                     'mensagem': mensagem}
        return jsonify(dados)

    elif request.method == 'DELETE':
        tasks.pop(id)
        return jsonify({'status': 'Sucesso!',
                        'mensagem': 'Registro excluído.'})


if __name__ == '__main__':
    app.run(debug=True)
