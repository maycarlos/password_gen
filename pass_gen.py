#!/usr/bin/env python3

import random
import string
import getpass
import time
import click
import database_interact

#Precisa de ser instalada previamente -> pip install alive_progress
from alive_progress import alive_bar


# Todas as preparações para fazer a palavra passe

def password_lenght():
    try:
        return int(input('Insira o tamanho da password que deseja obter: '))
    except ValueError:
        print("Por favor insira corretamento o o tamanho que deseja.")
        time.sleep(0.5)
        return password_lenght()

def chosen_password_parameters():
    """
    Pedir ao utilizador os parâmetros que quer na sua password.  
    """
    quer_letras = input('Queres letras na password?(True/False): ')
    quer_numeros = input('Queres números na password?(True/False): ')
    quer_puntuaction = input('Queres pontuação no password?(True/False): ')

    resultado = [quer_letras, quer_numeros, quer_puntuaction]
    #Substitui todas as strings com Booleans
    for i,j in enumerate(resultado):
        try:
            resultado[i] = eval(j.title())
        except:
            print("O valor que introduziu não permite realizar a função.\nPor favor insira True ou False nos lugares adequados.")
            time.sleep(1)
            return chosen_password_parameters()

    return resultado
    
def characters_included(escolha):
    """
    Dá nos uma string com o caracteres que desejamos que sejam incluídos na password.
    Em função da lista que resulta da função chosen_password_parameters
    """
    letras = string.ascii_letters
    punctuation = string.punctuation
    numero = string.digits

    modelo_da_pass = ''
    modelo_da_pass += letras if escolha[0] else ''
    modelo_da_pass += numero if escolha[1] else ''
    modelo_da_pass += punctuation if escolha[2] else ''

    return modelo_da_pass

def generate_password(constituintes ,tamanho):
    """
    Depois de termos todos os parametros da password definidos.  
    Damos shufle a string com os constituintes e cortamos a string resultante em função do tamanho determinado
    """
    baralho = list(constituintes)
    random.shuffle(baralho)
    pass_final = ''.join(baralho)

    #Aqui apenas pego nos primeiros n caracteres da string baralhada, se calhar devo escolher letras aleatoriamente da string(?)
    return pass_final[:tamanho]

def export_password(palavra_pass):
    """
    Depois de gerar a palavra passe, exportá-la para uma db.   
    """
    destino = str(input("Onde é que esta password vai ser utilizada? "))

    database_interact.dump_password(getpass.getuser().title(), destino, palavra_pass)


# Parte do CLI com o módulo Click

@click.group()
def menu():
    pass

@menu.command('get')
def get_password():
    """
    Aceder a DB e ter a palavra passe que queremos ver.
    """
    database_interact.get_passwords()

@menu.command('see')
def see_save():
    """
    Ver todas as palavras passe que estão guardadas na DB
    """
    database_interact.see_save()

@menu.command('clear')
def clear_data():
    """
    Apagar todas a palavras passe que estão guardadas na DB
    """
    action = int(input('Deseja:\n 1-Apagar um palavra passe especifica\n 2-Apagar todas a palavras que estão guardadas? '))

    if action == 1:
        database_interact.see_save()

        eraser_index = int(input('Qual é a palavra passe que deseja eliminar? '))

        try:
            database_interact.delete_one(eraser_index)
        except:
            print("Uh Oh :/")

    elif action == 2 :
        database_interact.delete_all()
        print('Done!', end='\n')


@menu.command('create', short_help='cria a palavra passe')
def password_construct():
    """
    Função que acaba por contruir a palavra passe e exporta a mesma para a base de dados. 
    """
    database_interact.table_creation()

    tamanho = password_lenght()
    parametros_desejados = chosen_password_parameters()
    molde_password = characters_included(parametros_desejados)
    password_desejada = generate_password(molde_password, tamanho)
    
    #Sem utilidade nenhuma, apenas acho engraçado ter barras
    with alive_bar(100, 'A gerar a password') as bar:
        for _ in range(100):
            time.sleep(0.01)
            bar()
    
    print(f"\nUser:\t\t{getpass.getuser().title()}.\nPassword:\t{password_desejada}")

    export_password(password_desejada)

    print("\nDone!")

if __name__ =='__main__':
    menu()