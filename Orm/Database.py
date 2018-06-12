#Database.py

from sqlalchemy.orm import sessionmaker, scoped_session
from DBClasses import Base, Endereco, engine, Pessoa

DBSession = sessionmaker(bind=engine)    

def addPessoa(pessoa):
    session = DBSession()
    session.add(pessoa)
    session.commit()
    session.close()
    return pessoa

def deletePessoa(pessoa):
    session = DBSession()
    session.delete(pessoa)
    session.commit()
    session.close()

def findAllPessoas():
    session = DBSession()
    pessoas = session.query(Pessoa).all()
    session.close()
    return pessoas

def findPessoaByPessoaId(pessoa_id):
    session = DBSession()
    pessoa = session.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    session.close()
    return pessoa

def addEndereco(endereco):
    session = DBSession()
    session.add(endereco)
    session.commit()
    session.close()
    return endereco

def deleteEndereco(endereco):
    session = DBSession()
    session.delete(endereco) 
    session.commit()
    session.close()

def findAllEnderecoByPessoaId(pessoa_id_):
    session = DBSession()
    enderecos = session.query(Endereco).filter(Endereco.pessoa_id == pessoa_id_).all()
    session.close()
    return enderecos

def findEnderecoByEnderecoId(endereco_id_):
    session = DBSession()
    endereco = session.query(Endereco).filter(Endereco.id == endereco_id_).first()
    session.close()
    return endereco
