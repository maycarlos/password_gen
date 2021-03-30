import random
import string
import json 
import getpass
import time

#Precisa de ser instalada previamente -> pip install alive_progress
from alive_progress import alive_bar

#Não tenho a certeza se devo meter isto dentro da função chosen_password_parameters ou deixo aqui fora
letras = string.ascii_letters
punctuation = string.punctuation
numero = string.digits

#não se usa a string.printable() para dar a oportunidade de poder escolher o que deseja ter na pass

def password_lenght():
    return int(input('Insira o tamanho da password que deseja obter: '))

def chosen_password_parameters():
    """
    Pedir ao utilizador os parametros que quer na sua password
    Letras = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    numero = 0123456789
    """
    quer_letras = input('Queres letras na password?(True/False): ')
    quer_numeros = input('Queres números na password?(True/False): ')
    quer_puntuaction = input('Queres pontuação no password?(True/False): ')

    #Percebi que não pode usar sets nem tuples, porque são immutable
    resultado = [quer_letras, quer_numeros, quer_puntuaction]

    #Substitui todos as strings com Booleans
    for i,j in enumerate(resultado):
        resultado[i] = eval(j)

    return resultado
    
def characters_included(escolha):
    """
    Dá nos uma string com o caracteres que desejamos que sejam incluídos na password.
    Em função da lista que resulta da função chosen_password_parameters
    """
    modelo_da_pass = ''
    modelo_da_pass += letras if escolha[0] else ''
    modelo_da_pass += numero if escolha[1] else ''
    modelo_da_pass += punctuation if escolha[2] else ''

    return modelo_da_pass

def generate_password(constituintes ,tamanho = 8):
    """
    Depois de termos todos os parametros da password definidos
    Damos shufle a string com os constituintes e cortamos a string resultante em função do tamanho determinado
    """
    baralho = list(constituintes)
    random.shuffle(baralho)

    pass_final = ''.join(baralho)

    #Aqui apenas pego nos primeiros 8 caracteres da string baralhada, se calhar devo escolher letras aleatoriamente da string(?)
    return pass_final[:tamanho]

def main():
    tamanho = password_lenght()

    parametros_desejados = chosen_password_parameters()
    molde_password = characters_included(parametros_desejados)

    password_desejada = generate_password(molde_password, tamanho)
    
    #Sem utilidade nenhuma, apenas acho engraçado ter barras em trabalhos 
    with alive_bar(100, 'A gerar a password') as bar:
        for _ in range(100):
            time.sleep(0.01)
            bar()

    print(f'User:\t\t{getpass.getuser().title()}.\nPassword:\t{password_desejada}') 

if __name__ == '__main__':
    main()