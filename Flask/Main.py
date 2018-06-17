# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World', 200

@app.route('/hello')
@app.route('/hello/<nome>')
@app.route('/hello/<nome>/<sobrenome>')
def echo_name(nome = None, sobrenome = None):
    if nome == None:
        nome = 'Visitante'
    if sobrenome == None:
        sobrenome = ' '
    return 'Ola ' + nome + ' ' + sobrenome, 200

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
    soma = num1 + num2
    return 'Soma: ' + str(soma), 200

@app.route('/subt/<int:num1>/<int:num2>')
def subt(num1, num2):
    subt = num1 - num2
    return 'Subtracao: ' + str(subt), 200

@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1, num2):
    mult = num1 * num2
    return 'Multiplicacao: ' + str(mult), 200

@app.route('/divi/<int:num1>/<int:num2>')
def divi(num1, num2):
    divi = num1 / num2
    return 'Divisao: ' + str(divi), 200

app.run(debug=True, use_reloader=True)