# -*- coding: utf-8 -*-

from DBClasses import Contato, Endereco, Telefone
import Database as db

def validar_menu(inicio, fim):
    while True:
        try:
            valor = int(input('\nEscolha uma opção: '))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
    print('\n--- Menu ---')
    print('1 - Listar ')
    print('2 - Novo ')
    print('3 - Alterar ')
    print('4 - Deletar ')
    print('5 - Sair ')
    return validar_menu(1, 5)

def menu_generico(funcao):
    print('\n--- Menu {}---'.format(funcao))
    print('1 - {} Contato '.format(funcao))
    print('2 - {} Endereco '.format(funcao))
    print('3 - {} Telefone '.format(funcao))
    print('4 - Voltar ')
    return validar_menu(1, 4)

print('\n---Seja Bem-Vindo a Agenda!---\n')

while True:
    opcao = menu()
    if opcao == 1:
        db.print_contatos()
    elif opcao == 2:
        voltar = False
        while voltar != True:
            voltar = False
            opc = menu_generico('Novo')
            if opc == 1:
                db.add_contato()
            elif opc == 2:
                db.add_endereco()
            elif opc == 3:
                db.add_telefone()
            elif opc == 4:
                voltar = True
    elif opcao == 3:
        voltar = False
        while voltar != True:
            opc = menu_generico('Alterar')
            if opc == 1:
                db.print_contatos()
                db.update_contato()
            elif opc == 2:
                db.print_contatos()
                db.update_endereco()
            elif opc == 3:
                db.print_contatos()
                db.update_telefone()
            elif opc == 4:
                voltar = True
    elif opcao == 4:
        voltar = False
        while voltar != True:
            opc = menu_generico('Deletar')
            if opc == 1:
                db.print_contatos()
                db.delete_contato()
                db.print_contatos()
            elif opc == 2:
                db.print_contatos()
                db.delete_endereco()
                db.print_contatos()
            elif opc == 3:
                db.print_contatos()
                db.delete_telefone()
                db.print_contatos()
            elif opc == 4:
                voltar = True
    elif opcao == 5:
        break

print('\n--- Obrigado por usar os serviços da Agenda!!! ---')