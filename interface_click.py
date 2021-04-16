#!/usr/bin/env python

import click
import pass_gen

@click.group()
def menu():
    pass

@menu.command()
def create():
    """
    Crie uma palavra passe e guarde a mesma no ficheiro.
    """
    pass_gen.password_construct()

@menu.command()
# A keyword que está no decorator tem que ter o mesmo nome que o parâmetro da função
def get():
    """
    Ver uma palavra passe armazenada. Use 0 para ver a ultima pass que criou.
    TODO Meter uma lista na help string com as passes que tenho guardadas
    """
    pass_gen.get_password()

@menu.command()
def see():
    """
    Ver as palavras passe guardadas no ficheiro.
    """
    pass_gen.see_save()

@menu.command()
def clear():
    """
    Apagar todas as palavras passe que estão guardadas no ficheiro.
    """
    pass_gen.clear_data()

if __name__ == "__main__":
    menu()
