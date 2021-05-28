#!/usr/bin/env python3

import sqlite3
import pyperclip

conn = sqlite3.connect('pass_gen/passwords/database.sqlite')

curs = conn.cursor()

def table_creation():
    try:
        curs.execute("""
        CREATE TABLE IF NOT EXISTS user_passwords(
        user TEXT,
        site TEXT,
        password TEXT
        )""")
    except sqlite3.OperationalError:
        return None

def dump_password(user, target_site, user_password):
    with conn:
        curs.execute("INSERT INTO user_passwords VALUES (:username, :site, :password)",
         {'username':user, 'site':target_site, 'password':user_password})

def see_save():
    info = get_info()
    lista = [f'{n} - {i[0]} para o site {i[1]}' for n, i in enumerate(info, 1)]
    for i in lista:
        print(i)

def get_passwords():
    info = get_info()
    lista = [f'{n} - {i[0]} para o site {i[1]}' for n, i in enumerate(info, 1)]
    for i in lista:
        print(i)
    
    index = int(input("Qual é a palavra passe que quer? "))

    try:
        password = info[index-1][2]
        pyperclip.copy(password)
        print("A palavra pass foi adicionada à área de transferência.")
    except:
        print('Fiz algo não muito bom!')

def get_info():
    curs.execute("SELECT * FROM user_passwords")
    return curs.fetchall()

def delete_one(index):
    info = get_info()
    target_site = info[index-1][1]

    with conn:
        curs.execute("DELETE from user_passwords WHERE site = :site",
        {'site':target_site})

def delete_all():
    with conn:
        curs.execute("DELETE from user_passwords")
