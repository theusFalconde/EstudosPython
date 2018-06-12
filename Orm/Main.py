#Main.py

from DBClasses import Pessoa, Endereco
import Database as db

def createPessoa():
    pessoa = db.addPessoa(Pessoa('Matheus'))
    db.addEndereco(Endereco('Rua Gramona', 159, 83328290, pessoa))

    pessoa2 = db.addPessoa(Pessoa('Maria'))
    db.addEndereco(Endereco('Rua Joao Zaiter', 702, 83324210, pessoa2))
    db.addEndereco(Endereco('Rua Joao Zaiter2', 7022, 83324211, pessoa2))

def readPessoas():
    pessoas = db.findAllPessoas()

    for p in pessoas:
        enderecos = db.findAllEnderecoByPessoaId(p.id)

        for e in enderecos:
            print('Id: {0:2d}, Rua: {1:20}, Numero: {2:10}, Cep: {3:10}, Pessoa: {4:10}, Pessoa id: {5:3}'.format(e.id, e.rua, e.numero, e.cep, e.pessoa.nome, e.pessoa.id))

def updatePessoa(id, nome):
    pessoa = db.findPessoaByPessoaId(id)
    print('Nome: {0:20}'.format(pessoa.nome))
    pessoa.nome = nome
    db.addPessoa(pessoa)
    p = db.findPessoaByPessoaId(id)
    print('Nome: {0:20}'.format(p.nome)) 

def deletePessoa(id):
    pessoa = db.findPessoaByPessoaId(id)
    enderecos = db.findAllEnderecoByPessoaId(pessoa.id)
    for e in enderecos:
        db.deleteEndereco(e)
    db.deletePessoa(pessoa)

#createPessoa()

#readPessoas()

#updatePessoa(2, 'Joana')

#deletePessoa(1)