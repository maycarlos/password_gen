import pass_gen
from simple_term_menu import TerminalMenu

"""
É isto que eu queria que o curses fizesse mas pronto encontrei outro modulo que o cansegue fazer bem.  
Este modulo não funciona para windows tho por isso tenho que me lembrar de utlizar este menu em WSL
"""
opções = {"Criar palavra passe":"pass_gen.password_construct()",
    "Copiar palavras passe":"pass_gen.get_password()",
    "Ver palavras passe guardadas":"pass_gen.see_save()",
    "Apagar as palavras passe guardadas":"pass_gen.clear_data()"
    }

real = [i for i in opções.keys()]
real.append("Sair")

my_menu = TerminalMenu(real)
quitting = False

while quitting == False:
    menu_entry_index = my_menu.show()
    optionsChoice = real[menu_entry_index]
    
    if optionsChoice == "Sair":
        quitting = True
    else:
        eval(opções[optionsChoice])
        break
        