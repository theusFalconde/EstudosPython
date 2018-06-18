# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from DBClasses import Contato, Endereco, Telefone
import Database as db

app = Flask(__name__)

@app.route('/')
def agenda():
    mensagem = request.args.get('mensagem')
    contatos = db.find_all_contatos()
    return render_template('index.html', contatos=contatos, mensagem=mensagem)

@app.route('/telefones/<int:contato_id>')
def telefones(contato_id = None):
    mensagem = request.args.get('mensagem')
    telefones = db.find_all_telefone_by_contato_id(contato_id)
    contato = db.find_contato_by_contato_id(contato_id)
    return render_template('telefones.html', telefones=telefones, contato=contato, mensagem=mensagem)

@app.route('/enderecos/<int:contato_id>')
def enderecos(contato_id = None):
    mensagem = request.args.get('mensagem')
    enderecos = db.find_all_endereco_by_contato_id(contato_id)
    contato = db.find_contato_by_contato_id(contato_id)
    return render_template('enderecos.html', enderecos=enderecos, contato=contato, mensagem=mensagem)

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

@app.route('/cadastrartelefone/<int:contato_id>/<int:telefone_id>', methods = ['GET', 'POST'])
@app.route('/cadastrartelefone/<int:contato_id>', methods = ['GET', 'POST'])
def cadastrar_telefone(contato_id = None, telefone_id = None):
    try:
        if request.method == 'GET':
            if contato_id != None and telefone_id == None:
                contato = db.find_contato_by_contato_id(contato_id)
                telefone = Telefone('', '', contato)
            else:
                contato = db.find_contato_by_contato_id(contato_id)
                telefone = db.find_telefone_by_telefone_id(telefone_id)
            return render_template('cadastrartelefone.html', contato=contato, telefone=telefone)
        else:
            mensagem = 'Telefone adicionado com sucesso!'
            contato = db.find_contato_by_contato_id(contato_id)
            id = request.form.get('id')
            telefone = Telefone('', '', contato)
            if id != 'None':
                mensagem = 'Telefone atualizado com sucesso!'
                telefone = db.find_telefone_by_telefone_id(id)
            telefone.telefone = request.form.get('telefone')
            telefone.tipo_telefone = request.form.get('tipo_telefone')
            db.add(telefone)
            return redirect(url_for('telefones', contato_id=contato_id, mensagem=mensagem))
    except Exception:
        mensagem = 'Ocorreu um erro, tente novamente mais tarde!'
        return redirect(url_for('telefones', contato_id=contato_id, mensagem=mensagem))

@app.route('/cadastrarendereco/<int:contato_id>/<int:endereco_id>', methods = ['GET', 'POST'])
@app.route('/cadastrarendereco/<int:contato_id>', methods = ['GET', 'POST'])
def cadastrar_endereco(contato_id = None, endereco_id = None):
    try:
        if request.method == 'GET':
            if contato_id != None and endereco_id == None:
                contato = db.find_contato_by_contato_id(contato_id)
                endereco = Endereco('', '', '', contato)
            else:
                contato = db.find_contato_by_contato_id(contato_id)
                endereco = db.find_endereco_by_endereco_id(endereco_id)
            return render_template('cadastrarendereco.html', contato=contato, endereco=endereco)
        else:
            mensagem = 'Endereço adicionado com sucesso!'
            contato = db.find_contato_by_contato_id(contato_id)
            id = request.form.get('id')
            endereco = Endereco('', '', '', contato)
            if id != 'None':
                mensagem = 'Endereço atualizado com sucesso!'
                endereco = db.find_endereco_by_endereco_id(id)
            endereco.rua = request.form.get('rua')
            endereco.numero = request.form.get('numero')
            endereco.cep = request.form.get('cep')
            db.add(endereco)
            return redirect(url_for('enderecos', contato_id=contato_id, mensagem=mensagem))
    except Exception:
        mensagem = 'Ocorreu um erro, tente novamente mais tarde!'
        return redirect(url_for('enderecos', contato_id=contato_id, mensagem=mensagem))

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

@app.route('/deletartelefone/<int:contato_id>/<int:telefone_id>')
def deletar_telefone(contato_id = None, telefone_id = None):
    if telefone_id != None:
        telefone = db.find_telefone_by_telefone_id(telefone_id)
        if(telefone != None):
            db.delete(telefone)
            return redirect(url_for('telefones', contato_id=contato_id, mensagem='Telefone deletado com sucesso!'))
        else: 
            return redirect(url_for('telefones', contato_id=contato_id, mensagem='Telefone não encontrado!'))
    else:
        return redirect(url_for('telefones', contato_id=contato_id, mensagem='Telefone não encontrado!'))

@app.route('/deletarendereco/<int:contato_id>/<int:endereco_id>')
def deletar_endereco(contato_id = None, endereco_id = None):
    if endereco_id != None:
        endereco = db.find_endereco_by_endereco_id(endereco_id)
        if(endereco != None):
            db.delete(endereco)
            return redirect(url_for('enderecos', contato_id=contato_id, mensagem='Endereco deletado com sucesso!'))
        else: 
            return redirect(url_for('enderecos', contato_id=contato_id, mensagem='Endereco não encontrado!'))
    else:
        return redirect(url_for('enderecos', contato_id=contato_id, mensagem='Endereco não encontrado!'))
    
@app.route('/favicon.ico')
def hello():
    return redirect(url_for('static', filename='favicon.ico'), code=200)

app.run(debug=True, use_reloader=True)