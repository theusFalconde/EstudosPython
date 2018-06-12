#DBClasses.py

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Contato(Base):
    __tablename__ = 'contato'
    id = Column(Integer, primary_key = True)
    nome = Column(String(255), nullable = False)
    email = Column(String(255))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key = True)
    rua = Column(String(255))
    numero = Column(String(255))
    cep = Column(String(255), nullable = False)
    contato_id = Column(Integer, ForeignKey('contato.id', ondelete='CASCADE'))
    contato = relationship(Contato, lazy='subquery', backref=backref('endereco', cascade='all,delete'))

    def __init__(self, rua, numero, cep, contato):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.contato = contato

class Telefone(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key = True)
    telefone = Column(String(255), nullable = False)
    tipo_telefone = Column(String(255), nullable = False)
    contato_id = Column(Integer, ForeignKey('contato.id', ondelete='CASCADE'))
    contato = relationship(Contato, lazy='subquery', backref=backref('telefone', cascade='all,delete'))

    def __init__(self, telefone, tipo_telefone, contato):
        self.telefone = telefone
        self.tipo_telefone = tipo_telefone
        self.contato = contato

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)