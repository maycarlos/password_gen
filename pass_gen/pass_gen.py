#!/usr/bin/env python3

import time
import click
from dataclasses import dataclass
from alive_progress import alive_bar
from . import database_interact
from . import password_class

@click.group()
def menu():
    pass

@menu.command('get', short_help='Obter uma palavra passe da DB')
def get_password():
    """
    Aceder a DB e obter a palavra passe que queremos ver.
    """
    database_interact.get_passwords()

@menu.command('see', short_help='Ver as palavras passe guardadas')
def see_save():
    """
    Ver as palavras passe que estão guardadas na DB
    """
    database_interact.see_save()

@menu.command('delete', short_help='Apagar palavras passe')
@click.option('--all', '-a', is_flag=True)
@click.option('--one', '-o', is_flag=True)
def delete_data(one, all):
    """
    Apagar palavras passe que estão guardadas na DB
    -a / --all para apagar todas palavras passe que estão na DB
    -o / --one para apagar só uma palavra passe 
    """
    if one:
        database_interact.see_save()
        eraser_index = int(input('Qual é a palavra passe que deseja eliminar? '))

        try:
            database_interact.delete_one(eraser_index)
            
        except:
            print("Uh Oh :/")
    if all:
        database_interact.delete_all()

    print('Done!', end='\n')


@menu.command('create', short_help='Constroi a palavra passe')
def main():
    """
    Função que acaba por contruir a palavra passe e exporta a mesma para a base de dados.
    """
    database_interact.table_creation()

    password = password_class.Password()
    password.construct()

    #Sem utilidade nenhuma, apenas acho engraçado ter barras
    with alive_bar(100, 'A gerar a password') as bar:
        for _ in range(100):
            time.sleep(0.01)
            bar()

    database_interact.insert_info(password.user, password.destination, password.password)

    print("\nDone!")

if __name__ =='__main__':
    menu()