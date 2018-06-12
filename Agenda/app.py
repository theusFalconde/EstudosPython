from flask import Flask, render_template, jsonify, request, redirect, url_for
from DBClasses import Contato, Endereco, Telefone
import Database as db

app = Flask(__name__)

@app.route('/')
def agenda():
    mensagem = request.args.get('mensagem')
    contatos = db.find_all_contatos()
    return render_template('index.html', contatos=contatos, mensagem=mensagem)

@app.route('/cadastrarcontato/<int:contato_id>')
@app.route('/cadastrarcontato', methods = ['GET', 'POST'])
def cadastrar_contato(contato_id = None):
    try:
        if request.method == 'GET':
            if contato_id == None:
                contato = Contato('', '')
            else:
                contato = db.find_contato_by_contato_id(contato_id)
            return render_template('cadastrarcontato.html', contato=contato)
        else:
            mensagem = 'Contato adicionado com sucesso!'
            id = request.form.get('id')
            contato = Contato('', '')
            if id != 'None':
                mensagem = 'Contato atualizado com sucesso!'
                contato = db.find_contato_by_contato_id(id)
            contato.nome = request.form.get('nome')
            contato.email = request.form.get('email')
            db.add(contato)
            return redirect(url_for('agenda', mensagem=mensagem))
    except Exception:
        mensagem = 'Ocorreu um erro, tente novamente mais tarde!'
        return redirect(url_for('agenda', mensagem=mensagem))

@app.route('/deletarcontato/<int:contato_id>')
def deletar_contato(contato_id = None):
    if contato_id != None:
        contato = db.find_contato_by_contato_id(contato_id)
        if contato != None:
            db.delete(contato)
            return redirect(url_for('agenda', mensagem='Contato deletado com sucesso!'))
        else: 
            return redirect(url_for('agenda', mensagem='Contato não encontrado!'))
    else:
        return redirect(url_for('agenda', mensagem='Contato não encontrado!'))
    

app.run(debug=True, use_reloader=True)