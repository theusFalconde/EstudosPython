# Database.py

from sqlalchemy.orm import sessionmaker, scoped_session
from DBClasses import Endereco, engine, Contato, Telefone

DBSession = sessionmaker(bind=engine)

def add(obj):
    session = DBSession()
    session.add(obj)
    session.commit()
    session.refresh(obj)
    session.close()
    return obj

def add_contato():
    try:
        print('\nAdicionando Novo Contato: \n')
        nome = input('Nome: ')
        email = input('E-mail: ')
        contato = Contato(nome, email)
        add(contato)
        print('\nContato adicionado com sucesso!!!')
        print('\nId: {} \nNome: {} \nEmail: {}'.format(contato.id, contato.nome, contato.email))
    except Exception:
        print('Houve um erro ao adicionar o novo Contato!')

def add_endereco():
    try:
        print('\nAdicionando Novo Endereço: \n')
        id_contato = input('Id Contato: ')
        contato = find_contato_by_contato_id(id_contato)
        if contato != None:
            rua = input('Rua: ')
            numero = input('Número: ')
            cep = input('CEP: ')
            endereco = Endereco(rua, numero, cep, contato)
            add(endereco)
            print('\nEndereço adicionado com sucesso!!!')
            print('\nId: {} \nNome: {} \nEmail: {}'.format(contato.id, contato.nome, contato.email))
            print('\n\tEndereço:')
            print('\t\tId: {} \n\t\tRua: {} \n\t\tNúmero: {} \n\t\tCEP: {}'.format(endereco.id, endereco.rua, endereco.numero, endereco.cep))
        else:
            print('\nContato não encontrado!\n')
    except Exception:
        print('Houve um erro ao adicionar o novo Endereco!')

def add_telefone():
    try:
        print('\nAdicionando Novo Telefone: \n')
        id_contato = input('Id Contato: ')
        contato = find_contato_by_contato_id(id_contato)
        if contato != None:
            tipo_telefone = input('Tipo Telefone: ')
            telefone = input('Telefone: ')
            telefone = Telefone(telefone, tipo_telefone, contato)
            add(telefone)
            print('\nContato adicionado com sucesso!!!')
            print('\nId: {} \nNome: {} \nEmail: {}'.format(contato.id, contato.nome, contato.email))
            print('\n\tTelefone:')
            print('\t\tId: {}, \n\t\tTipo Contato: {} \n\t\tTelefone: {}'.format(telefone.id, telefone.tipo_telefone, telefone.telefone))
        else:
            print('\nContato não encontrado!\n')
    except Exception:
        print('Houve um erro ao adicionar o novo Telefone!')

def update_contato():
    try:
        print('\nAlterando Contato: \n')
        id_contato = input('Id Contato: ')
        contato = find_contato_by_contato_id(id_contato)
        if contato != None:
            print('\nContato:')
            print('\nId: {} \nNome: {} \nEmail: {}\n'.format(contato.id, contato.nome, contato.email))
            contato.nome = input('Nome: ')
            contato.email = input('E-mail: ')
            add(contato)
            print('\nContato adicionado com sucesso!!!')
            print('\nContato:')
            print('\nId: {} \nNome: {} \nEmail: {}'.format(contato.id, contato.nome, contato.email))
        else:
            print('\nContato não encontrado!\n')
    except Exception:
        print('\nHouve um erro ao alterar o Contato!')

def update_endereco():
    try:
        print('\nAlterando Endereço: \n')
        id_endereco = input('Id Endereço: ')
        endereco = find_endereco_by_endereco_id(id_endereco)
        if endereco != None:
            print('\nEndereço:')
            print('\tId: {} \n\tRua: {} \n\tNúmero: {} \n\tCEP: {}\n'.format(endereco.id, endereco.rua, endereco.numero, endereco.cep))
            endereco.rua = input('Rua: ')
            endereco.numero = input('Número: ')
            endereco.cep = input('CEP: ')
            add(endereco)
            print('\nEndereço alterado com sucesso!!!')
            print('\nEndereço:')
            print('\tId: {} \n\tRua: {} \n\tNúmero: {} \n\tCEP: {}'.format(endereco.id, endereco.rua, endereco.numero, endereco.cep))
        else:
            print('\nEndereço não encontrado!\n')
    except Exception:
        print('\nHouve um erro ao alterar o Endereço!')

def update_telefone():
    try:
        print('\nAlterando Telefone: \n')
        id_telefone = input('Id Telefone: ')
        telefone = find_telefone_by_telefone_id(id_telefone)
        if telefone != None:
            print('\nTelefone:')
            print('\tId: {}, \n\tTipo Contato: {} \n\tTelefone: {}\n'.format(telefone.id, telefone.tipo_telefone, telefone.telefone))
            telefone.tipo_telefone = input('Tipo Telefone: ')
            telefone.telefone = input('Telefone: ')
            add(telefone)
            print('\nTelefone alterado com sucesso!!!')
            print('\nTelefone:')
            print('\tId: {}, \n\tTipo Contato: {} \n\tTelefone: {}'.format(telefone.id, telefone.tipo_telefone, telefone.telefone))
        else:
            print('\nTelefone não encontrado!\n')
    except Exception:
        print('\nHouve um erro ao alterar o Telefone!')

def delete(obj):
    session = DBSession()
    session.delete(obj)
    session.commit()
    session.close()

def delete_contato():
    try:
        print('\nDeletando Contato: \n')
        id_contato = input('Id Contato: ')
        contato = find_contato_by_contato_id(id_contato)
        if contato != None:
            delete(contato)
        else:
            print('\nContato não encontrado!\n')
    except Exception:
        print('Houve um erro ao deletar o Contato!')

def delete_endereco():
    try:
        print('\nDeletando Endereco: \n')
        id_endereco = input('Id Endereço: ')
        endereco = find_endereco_by_endereco_id(id_endereco)
        if endereco != None:
            delete(endereco)
        else:
            print('\nEndereço não encontrado!\n')
    except Exception:
        print('Houve um erro ao deletar o Endereço!')

def delete_telefone():
    try:
        print('\nDeletando Telefone: \n')
        id_telefone = input('Id Telefone: ')
        telefone = find_telefone_by_telefone_id(id_telefone)
        if telefone != None:
            delete(telefone)
        else:
            print('\nTelefone não encontrado!\n')
    except Exception:
        print('Houve um erro ao deletar o Telefone!')

def find_all_contatos():
    session = DBSession()
    contatos = session.query(Contato).all()
    session.close()
    return contatos

def print_contatos():
    contatos = find_all_contatos()
    print('\n --- Contatos --- \n')
    if(len(contatos) == 0):
        print('Nenhum contato na sua Agenda!!!')
    else:
        for c in contatos:
            print('Id: {} \nNome: {} \nEmail: {}'.format(c.id, c.nome, c.email))
            enderecos = find_all_endereco_by_contato_id(c.id)
            print('\tEndereços:')
            for e in enderecos:
                print('\t\tId: {} \n\t\tRua: {} \n\t\tNúmero: {} \n\t\tCEP: {}\n'.format(e.id, e.rua, e.numero, e.cep))
            telefones = find_all_telefone_by_contato_id(c.id)
            print('\tTelefones:')
            for t in telefones:
                print('\t\tId: {}, \n\t\tTipo Contato: {} \n\t\tTelefone: {}\n'.format(t.id, t.tipo_telefone, t.telefone))
    print('\n')

def find_contato_by_contato_id(contato_id):
    session = DBSession()
    contato = session.query(Contato).filter(Contato.id == contato_id).first()
    session.close()
    return contato

def find_all_endereco_by_contato_id(contato_id):
    session = DBSession()
    enderecos = session.query(Endereco).filter(Endereco.contato_id == contato_id).all()
    session.close()
    return enderecos

def find_endereco_by_endereco_id(endereco_id):
    session = DBSession()
    endereco = session.query(Endereco).filter(Endereco.id == endereco_id).first()
    session.close()
    return endereco

def find_all_telefone_by_contato_id(contato_id):
    session = DBSession()
    enderecos = session.query(Telefone).filter(Telefone.contato_id == contato_id).all()
    session.close()
    return enderecos

def find_telefone_by_telefone_id(telefone_id):
    session = DBSession()
    endereco = session.query(Telefone).filter(Telefone.id == telefone_id).first()
    session.close()
    return endereco