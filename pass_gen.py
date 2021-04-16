import random
import string
import getpass
import time
import json
import pyperclip

#Precisa de ser instalada previamente -> pip install alive_progress
from alive_progress import alive_bar

def password_lenght():
    #Começo a meter Try e excepts em todas as partes que requerem input humano? ou um tipo especifico de dados
    try:
        return int(input('Insira o tamanho da password que deseja obter: '))
    except ValueError:
        print("Por favor insira corretamento o o tamanho que deseja.")
        # Não sei porquê mas n estava a dar return ao númer que desejava sem este return. Se calhar deve ser por causa do return no try idk
        time.sleep(1)
        return password_lenght()

def chosen_password_parameters():
    """
    Pedir ao utilizador os parâmetros que quer na sua password.  
    
    Letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ". 

    punctuation = "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~".  

    número = "0123456789".
    """
    quer_letras = input('Queres letras na password?(True/False): ')
    quer_numeros = input('Queres números na password?(True/False): ')
    quer_puntuaction = input('Queres pontuação no password?(True/False): ')
    #não se usa a string.printable() para dar a oportunidade de poder escolher o que deseja ter na pass


    resultado = [quer_letras, quer_numeros, quer_puntuaction]

    #Substitui todas as strings com Booleans
    for i,j in enumerate(resultado):
        try:
            resultado[i] = eval(j.title())
        except:
            print("O valor que introduziu não permite realizar a função.\nPor favor insira True ou False nos lugares adequados")
            time.sleep(1)
            chosen_password_parameters()

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
    Depois de gerar a palavra passe, exporta-la para um ficheiro json.   
    ~Ainda não faço a minima de como é que deve formatar bem os ficheiros json.~  Já sei.  
    TODO Entender melhor o que está a passar nesta parte, so deixei assim porque funciona.  
    Como? não sei mas vamos nessa vanessa
    """
    destino = str(input("Onde é que esta password vai ser utilizada? "))

    def insert_data(dados):
        with open("passwords/save_files.json", 'w') as f:
            json.dump(dados, f, indent= 4)

    with open("passwords/save_files.json") as save:
        dados = json.load(save)
        infor_utilizador = dados["user"] 

        nova_informação = {
            "name":f"{getpass.getuser().title()}",
            "site":f"{destino}",
            "password":f"{palavra_pass}"
        }

        infor_utilizador.append(nova_informação)
    
    insert_data(dados)

def get_password():
    """
    Aceder ao ficheiro JSON e ter a palavra passe que queremos ver
    """
    with open("passwords/save_files.json", 'r') as p:
        users = json.load(p)
        infor_utilizador = users["user"]

        enumerador_de_passwords = zip(range(1, len(infor_utilizador)+1), infor_utilizador)

    escolhas = [f"{i} - {j.get('name')} para o {j.get('site')}" for i,j in enumerador_de_passwords]    
    
    for i in escolhas:
        print(i)

    index = int(input("Qual é a palavra passe que quer? "))

    try:
        verificar = infor_utilizador[index-1].get("password")
    except IndexError:
        print("ERRO. \nNão tem palavras pass guardadas nesta aplicação ou o número que inseriu não consta na lista.\nA sair do programa.")
        time.sleep(1)
        quit()

    try:
        print('{}'.format(escolhas[index-1])) 
        confirmar = str(input("É esta a pass?(y/n) "))
        try:
            if confirmar == "y":
                time.sleep(1)
                pyperclip.copy(verificar)
                print("A palavra pass foi adicionada à área de transferência.")
        except:
            return
    except TypeError:
        print("Por favor insira corretamente a password que deseja ver.")
        time.sleep(1)
        quit()

def see_save():
    """
    Ver todas as palavras passe que estão guardadas no ficheiro JSON
    """
    with open("passwords/save_files.json", 'r') as p:
        users = json.load(p)
        infor_utilizador = users["user"]

        enumerador_de_passwords = zip(range(1, len(infor_utilizador)+1), infor_utilizador)

    escolhas = [f"{i} - {j.get('name')} para o {j.get('site')}" for i,j in enumerador_de_passwords]   
    for i in escolhas:
        print(i)

def clear_data():
    """
    Apagar todas a palavras passe que estão guardadas no ficheiro JSON
    TODO Dar a opção de poder escolher qual delas é que o utilizador quer apagar 
    """
    with open("passwords/save_files.json", "w+") as save:
        save.write('''{
    "user": [

    ]
}
        ''')

    print("Todas as palavras passe foram apagadas")

def password_construct():
    """
    Função que acaba por contruir a palavra passe e exporta a mesma. 
    """
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

if __name__ == '__main__':
    password_construct()