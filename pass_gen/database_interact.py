#!/usr/bin/env python3

import sqlite3
from typing import Optional
import pyperclip

try:
    conn = sqlite3.connect('pass_gen/passwords/database.sqlite')
except:
    conn = sqlite3.connect('passwords/database.sqlite')
finally:
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


def get_info():
    curs.execute("SELECT * FROM user_passwords")
    return curs.fetchall()


def insert_info(user: str, target_site: str, user_password: str):
    with conn:
        curs.execute("INSERT INTO user_passwords VALUES (:username, :site, :password)",
                     {'username': user, 'site': target_site, 'password': user_password})


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
        password = info[index - 1][2]
        pyperclip.copy(password)
        print("A palavra pass foi adicionada à área de transferência.")
    except:
        print('Fiz algo não muito bom!')


def delete_info(index: Optional[int] = None, one: bool = False, everything: bool = False):
    if one:
        info = get_info()
        target_site = info[index - 1][1]

        with conn:
            curs.execute("DELETE from user_passwords WHERE site = :site",
                         {'site': target_site})
    if everything:
        with conn:
            curs.execute("DELETE from user_passwords")
