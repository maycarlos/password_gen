#!/usr/bin/env python3

import random
import string
import getpass
import time
import click
import database_interact

# not built in mas o setup.py trata disso
from alive_progress import alive_bar


# Todas as preparações para fazer a palavra passe

def password_lenght() -> int:
    try:
        return int(input('Insira o tamanho da password que deseja obter: '))
    except ValueError:
        print("Por favor insira corretamento o o tamanho que deseja.")
        time.sleep(0.5)
        return password_lenght()

def chosen_password_parameters() -> list:
    """
    Pedir ao utilizador os parâmetros que quer na sua password.
    """
    quer_letras = click.confirm('Queres letras na password? ', default='True')
    quer_numeros = click.confirm('Queres números na password? ', default='True')
    quer_puntuaction = click.confirm('Queres pontuação no password? ', default = 'True')

    resultado = [quer_letras, quer_numeros, quer_puntuaction]

    return resultado

def characters_included(escolha: list) -> str:
    """
    Dá nos uma string com o caracteres que desejamos que sejam incluídos na password.
    Em função da lista que resulta da função chosen_password_parameters
    """
    LETTERS = string.ascii_letters
    PUNCTUATION = string.punctuation
    DIGITS = string.digits

    modelo_da_pass = ''
    modelo_da_pass += LETTERS if escolha[0] else ''
    modelo_da_pass += DIGITS if escolha[1] else ''
    modelo_da_pass += PUNCTUATION if escolha[2] else ''
    
    return modelo_da_pass

def generate_password(constituintes: str ,tamanho : int) -> str:
    """
    Depois de termos todos os parametros da password definidos.
    Damos shufle a string com os constituintes e cortamos a string resultante em função do tamanho determinado
    """
    baralho = random.sample(constituintes, tamanho)
    random.shuffle(baralho)
    pass_final = ''.join(baralho)

    return pass_final

def export_password(palavra_pass) -> None:
    """
    Depois de gerar a palavra passe, exportá-la para uma db.
    """
    destino = str(input("Onde é que esta password vai ser utilizada? "))

    database_interact.dump_password(getpass.getuser().title(), destino, palavra_pass)


# Parte do CLI com o módulo Click
@click.group()
def menu():
    pass

@menu.command('get', short_help='Obter uma palavra passe da DB')
def get_password():
    """
    Aceder a DB e obter a palavra passe que queremos ver.
    """
    database_interact.get_passwords()

@menu.command('see', short_help='Ver as palavras passe guardadass')
def see_save():
    """
    Ver as palavras passe que estão guardadas na DB
    """
    database_interact.see_save()
#TODO ALterar isto para se poder pedir para apagar logo com um -a para all ou -o para um
@menu.command('clear', short_help='Apagar palavras passe')
@click.option('--ation', '-a', type = int, required = True)
def clear_data(action):
    """
    Apagar palavras passe que estão guardadas na DB
    action = (1) para apagar só 1 palavra pass
    action = (2) para apagar todas
    """
    if action == 1:
        database_interact.see_save()

        eraser_index = int(input('Qual é a palavra passe que deseja eliminar? '))

        try:
            database_interact.delete_one(eraser_index)
            print('Done!', end='\n')
        except:
            print("Uh Oh :/")

    elif action == 2 :
        database_interact.delete_all()
        print('Done!', end='\n')


@menu.command('create', short_help='Constroi a palavra passe')
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

    print(f"\nUser:\t\t{getpass.getuser().title()}\nPassword:\t{password_desejada}")

    export_password(password_desejada)

    print("\nDone!")

if __name__ =='__main__':
    menu()