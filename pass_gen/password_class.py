import random
import string
import click
from getpass import getuser
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Password:
    """Classe da palavra passe. Forma mais limpa de a criar e manusear"""

    user: str = getuser().title()
    destination: Optional[str] = None
    password: Optional[str] = None

    def __length(self) -> int:

        try:
            return int(input('Insira o tamanho da password que deseja obter: '))
        except ValueError:
            print("Por favor insira corretamente o o tamanho que deseja.")
            return self.__length()

    @staticmethod
    def parameters() -> List[bool]:
        """Pedir ao utilizador os parâmetros que quer incluir na sua password."""
        
        want_letters = click.confirm('Queres letras na password? ', default='True')
        want_digits = click.confirm('Queres números na password? ', default='True')
        want_punctuation = click.confirm('Queres pontuação no password? ', default='True')

        return [want_letters, want_digits, want_punctuation]

    @staticmethod
    def generate(choice: List[bool], size: int) -> str:
        """ Função que gera a palavra passe"""

        letters = string.ascii_letters
        punctuation = string.punctuation
        digits = string.digits

        constituintes = [letters, punctuation, digits]

        modelo_da_pass = [constituintes[n] for n, value in enumerate(choice) if value]

        baralho = random.sample(''.join(modelo_da_pass), size)
        random.shuffle(baralho)
        
        return ''.join(baralho)

    def construct(self) -> None:

        self.password = self.generate(size=self.__length(), choice=self.parameters())

        print(f"\nUser:\t\t{self.user}\nPassword:\t{self.password}", end='\n')
        
        self.destination = input("Onde é que esta password vai ser utilizada? ")
