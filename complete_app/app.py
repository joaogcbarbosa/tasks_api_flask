from flask import Flask, request, render_template
from flask_htmlmin import HTMLMIN
from jinja2.exceptions import UndefinedError
from tables import Pessoa, Tarefa, session

app = Flask(__name__)

app.config['MINIFY_HTML'] = True
htmlmin = HTMLMIN(app, remove_comments=True, remove_empty_space=True, disable_css_min=False)


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/tasks/')
def tasks():
    all_tasks = session.query(Tarefa).all()
    return render_template('tasks.html', tasks=all_tasks)


@app.get('/get-task/')
@app.post('/get-task/')
def get_task():
    id = request.form.get('id_tarefa')
    try:
        if request.method == 'POST':
            if id:
                task = session.query(Tarefa).filter_by(id_tarefa=id).first()
                return render_template('task.html', task=task)
        return render_template('get-task.html')
    except UndefinedError:
        mensagem = f'NÃO HÁ TAREFA VINCULADA AO ID {id}'
        return render_template('message.html', msg=mensagem)


@app.get('/post-task/')
@app.post('/post-task/')
def post_task():
    if request.method == 'POST':
        responsavel = request.form.get('name')
        tarefa = request.form.get('task')
        status = request.form.get('status')
        if responsavel and tarefa and status:
            Tarefa(nome_tarefa=tarefa, status=status, pessoa=Pessoa(nome_pessoa=responsavel)).save()
    return render_template('post-task.html')


@app.get('/put-task/')
@app.post('/put-task/')
def put_task():
    id = request.form.get('id_tarefa')
    status = request.form.get('status')
    try:
        if request.method == 'POST':
            if id and status:
                task = session.query(Tarefa).filter_by(id_tarefa=id).first()
                task.status = status
                task.save()
                return render_template('task.html', task=task)
        return render_template('put-task.html')
    except AttributeError:
        mensagem = f'NÃO HÁ TAREFA VINCULADA AO ID {id}'
        return render_template('message.html', msg=mensagem)


@app.get('/delete-task/')
@app.post('/delete-task/')
def delete_task():
    id = request.form.get('id_tarefa')
    try:
        if request.method == 'POST':
            if id:
                task = session.query(Tarefa).filter_by(id_tarefa=id).first()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id).first()
                task.delete()
                pessoa.delete()
                mensagem = f'TAREFA DE ID {id} EXCLUÍDA'
                return render_template('message.html', msg=mensagem)
        return render_template('delete-task.html')
    except AttributeError:
        mensagem = f'NÃO HÁ TAREFA VINCULADA AO ID {id}'
        return render_template('message.html', msg=mensagem)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
