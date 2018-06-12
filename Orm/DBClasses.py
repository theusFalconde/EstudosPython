#DBClasses.py

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key = True)
    nome = Column(String(250), nullable = False)

    def __init__(self, nome):
        self.nome = nome

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key = True)
    rua = Column(String(250))
    numero = Column(String(250))
    cep = Column(String(250), nullable = False)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa, lazy='subquery')

    def __init__(self, rua, numero, cep, pessoa):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.pessoa = pessoa

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)