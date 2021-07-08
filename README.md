# Password generator

Um básico gerador de passwords para treinar algumas coisas que fui aprendendo ao longo do tempo.  

## Depenências

Ao utilizar `pip install -e .` as dependências são todas instaladas mas é sempre bom referir:  

- [Click](https://github.com/pallets/click)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- [Alive_progress](https://github.com/rsalmei/alive-progress)

## Flow deste projecto

- Download -> `git clone https://github.com/maycarlos/password_gen`

- Mudar para a pasta `cd pass_gen`

- Criar virtualenv `virtualenv venv`

- Entrar no virtualenv `. venv/bin/activate`

- Ainda não tenho a certeza se se deve fazer isto mas no ficheiro `setup.py` já está especificado tudo o que é preciso para isto funcionar por isso é só fazer `pip install -e .` que todas as dependencies são logo instaladas  

- Depois usar o comando da seguinte forma: `pass_gen [commands]`

## Mais umas coisinhas para fazer

- [x] Perguntar onde é que esta pass vai ser utilizada e adicionar esta informação no output da da função.  
- [x] Aprender e guardar as passwords num ficheiro JSON(ou outro tipo de ficheiro lindo onde se possa guardar informação) acompanhadas com o ~~user~~, sítio onde é utilizada e claro ~~a password~~ encriptada(maybe?).  
- [X] Quero criar um menu para usar na command line. Usei click e o simple term menu que fez tudo o que eu queria do curses por isso vou utliliza-lo para o resto deste projeto  
- [x] Fazer todo o processo reverso quando quiser consultar as passwords quardadas.  
- [x] Começar a ver e trabalhar com databases (sqlite3 parece ser uma coisinha fixe para aprender alguma coisa de SQL).  
