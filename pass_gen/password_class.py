import random
import string
import click
from getpass import getuser
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Password:
    """Classe da palavra passe. Forma mais limpa de a criar e manusear"""

    user : str = getuser().title()
    destination : Optional[str] = None
    password : Optional[str] = None

    def __lenght(self) -> int:

        try:
            return int(input('Insira o tamanho da password que deseja obter: '))
        except ValueError:
            print("Por favor insira corretamento o o tamanho que deseja.")
            return self.password_lenght()

    def __parameters(self) -> List[bool]:
        """Pedir ao utilizador os parâmetros que quer incluir na sua password."""
        
        quer_letras = click.confirm('Queres letras na password? ', default='True')
        quer_numeros = click.confirm('Queres números na password? ', default='True')
        quer_puntuaction = click.confirm('Queres pontuação no password? ', default = 'True')

        return [quer_letras, quer_numeros, quer_puntuaction]

    def __generate(self, choice: List[bool], size: int) -> str:
        """ Função que gera a palavra passe"""

        LETTERS = string.ascii_letters
        PUNCTUATION = string.punctuation
        DIGITS = string.digits

        constituintes  = [LETTERS, PUNCTUATION, DIGITS]

        modelo_da_pass = [constituintes[n] for n, value in enumerate(choice) if value]

        baralho = random.sample(''.join(modelo_da_pass), size)
        random.shuffle(baralho)
        
        return ''.join(baralho)

    def construct(self) -> None:

        self.password = self.__generate(size = self.__lenght(), choice = self.__parameters())

        print(f"\nUser:\t\t{self.user}\nPassword:\t{self.password}", end='\n')
        
        self.destination = input("Onde é que esta password vai ser utilizada? ")