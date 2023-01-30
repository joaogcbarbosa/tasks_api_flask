from flask import Flask, request
from flask_restful import Api, Resource
from json import loads

app = Flask(__name__)
api = Api(app)

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


@app.route('/')
def home():
    return ('<h1>Página Inicial</h1>'
            '<h2><a href="http://127.0.0.1:5000/todas-tarefas/">Todas Tarefas</a><br></h2>'
            '<h3>Para pesquisar(GET) ou excluir(DELETE) tarefa por ID: http://127.0.0.1:5000/tarefa/"id"/</h3>'
            '<h3>Para inserir(POST) tarefa: http://127.0.0.1:5000/incluir-tarefa/</h3>'
            '<h3>Para alterar(PUT) somente o status: http://127.0.0.1:5000/alterar-status/"id"/</h3>')


class TodasTarefas(Resource):
    def get(self):
        return tasks


class Tarefa(Resource):
    def get(self, id):
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
        return dados

    def delete(self, id):
        tasks.pop(id)
        return {'status': 'Sucesso!',
                'mensagem': 'Registro excluído.'}


class IncluirTarefa(Resource):
    def post(self):
        dados = loads(request.data)
        dados['id'] = len(tasks)
        tasks.append(dados)
        return {'status': 'Sucesso!',
                'mensagem': 'Registro inserido.'}


class AlterarStatus(Resource):
    def put(self, id):
        dados = loads(request.data)
        tasks[id]['status'] = dados['status']
        return {'status': 'Sucesso!',
                'mensagem': 'Status alterado.'}


api.add_resource(TodasTarefas, '/todas-tarefas/')
api.add_resource(Tarefa, '/tarefa/<int:id>/')
api.add_resource(IncluirTarefa, '/incluir-tarefa/')
api.add_resource(AlterarStatus, '/alterar-status/<int:id>/')

if __name__ == '__main__':
    app.run()
