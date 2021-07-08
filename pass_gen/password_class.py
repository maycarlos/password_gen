import random
import getpass
import string
import click
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Password:
    """Classe da palavra passe. Forma mais limpa de a criar e manusear"""

    user : str = getpass.getuser().title()
    destination: Optional[str] = None
    password : Optional[str] = None

    def lenght(self) -> int:
        try:
            return int(input('Insira o tamanho da password que deseja obter: '))
        except ValueError:
            print("Por favor insira corretamento o o tamanho que deseja.")
            return self.password_lenght()

    def parameters(self) -> List[bool]:
        """Pedir ao utilizador os parâmetros que quer incluir na sua password."""
        quer_letras = click.confirm('Queres letras na password? ', default='True')
        quer_numeros = click.confirm('Queres números na password? ', default='True')
        quer_puntuaction = click.confirm('Queres pontuação no password? ', default = 'True')

        resultado = [quer_letras, quer_numeros, quer_puntuaction]

        return resultado

    def generate(self, choice: List[bool], size: int) -> str:
        """ Função que gera a palavra passe"""
        LETTERS = string.ascii_letters
        PUNCTUATION = string.punctuation
        DIGITS = string.digits

        constituintes  = [LETTERS, PUNCTUATION, DIGITS]

        modelo_da_pass = [ constituintes[n] for n, value in enumerate(choice) if value]

        baralho = random.sample(''.join(modelo_da_pass), size)
        random.shuffle(baralho)
        
        return ''.join(baralho)

    def construct(self) -> None:

        self.password = self.generate(size = self.lenght(), choice = self.parameters())

        print(f"\nUser:\t\t{self.user}\nPassword:\t{self.password}", end='\n')
        
        self.destination = input("Onde é que esta password vai ser utilizada? ")

