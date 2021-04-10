import click
import pass_gen

@click.group()
def menu():
    pass

@menu.command()
def create():
    """
    Crie uma palavra passe a guarde a no ficheiro JSON
    """
    pass_gen.main()

@menu.command()
# A keyword que está no decorator tem que ter o mesmo nome que o parâmetro da função
@click.option("-i", default = 1, help = "Diga o index da palavra passe que quer verificar.")
def get(i = None):
    """
    Ver uma palavra passe armazenada. Use 0 para ver a ultima pass que criou 
    TODO Meter uma lista na help string com as passes que tenho guardadas
    """
    pass_gen.get_pass(i)

@menu.command()
def clear():
    """
    Apagar todas as palavras passe que estão guardadas no ficheiro JSON
    """
    pass_gen.clear_data()

if __name__ == "__main__":
    menu()
