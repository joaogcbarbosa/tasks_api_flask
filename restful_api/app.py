from flask import Flask, request
from flask_restful import Api, Resource
from tables import Pessoa, Tarefa, session
import json

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        response = [{'Para visualizar todas tarefas': 'http://127.0.0.1:5000/tasks/',
                     'Para visualizar cada tarefa por Id': 'http://127.0.0.1:5000/task/id_here',
                     'Para incluir nova tarefa': 'http://127.0.0.1:5000/task/id_here',
                     'Para alterar status da tarefa por Id': 'http://127.0.0.1:5000/task/id_here',
                     'Para excluir tarefa por Id': 'http://127.0.0.1:5000/task/id_here'}]
        return response


class Tasks(Resource):
    def get(self):
        tarefas = session.query(Tarefa).all()
        response = [{'id_tarefa': tarefa.id_tarefa,
                     'pessoa': tarefa.pessoa.nome_pessoa,
                     'tarefa': tarefa.nome_tarefa,
                     'status': tarefa.status} for tarefa in tarefas]
        return response


class Task(Resource):
    def get(self, id):
        try:
            tarefa = session.query(Tarefa).filter_by(id_tarefa=id).first()
            response = {'id_tarefa': tarefa.id_tarefa,
                        'pessoa': tarefa.pessoa.nome_pessoa,
                        'tarefa': tarefa.nome_tarefa,
                        'status': tarefa.status}
        except AttributeError:
            response = {
                'status': 'Erro.',
                'mensagem': f'Não há tarefa vinculada ao id {id}.'
            }
        return response

    def post(self):
        data = json.loads(request.data)
        Tarefa(nome_tarefa=data['tarefa'],
               status=data['status'],
               pessoa=Pessoa(nome_pessoa=data['pessoa'])).save()
        response = {
            'status': 'Sucesso.',
            'mensagem': 'Registro inserido.'
        }
        return response

    def put(self, id):
        try:
            data = json.loads(request.data)
            tarefa = session.query(Tarefa).filter_by(id_tarefa=id).first()
            tarefa.status = data['status']
            tarefa.save()
            response = {
                'status': 'Sucesso.',
                'mensagem': 'Status alterado.'
            }
        except AttributeError:
            response = {
                'status': 'Erro.',
                'mensagem': f'Não há tarefa vinculada ao id {id}.'
            }
        return response

    def delete(self, id):
        try:
            tarefa = session.query(Tarefa).filter_by(id_tarefa=id).first()
            tarefa.delete()
            response = {
                'status': 'Sucesso.',
                'mensagem': 'Registro excluído.'
            }
        except AttributeError:
            response = {
                'status': 'Erro.',
                'mensagem': f'Não há tarefa vinculada ao id {id}.'
            }
        return response


api.add_resource(Home, '/')
api.add_resource(Tasks, '/tasks/')
api.add_resource(Task, '/task/<int:id>/', '/task/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
