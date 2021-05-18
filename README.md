# Password generator

Um básico gerador de passwords para treinar algumas coisas que fui aprendendo ao longo do tempo.  
Usa um módulo que tem que ser instalado previamente que é o [Alive Progress](https://github.com/rsalmei/alive-progress) de resto acho que é tudo built-in no python.


## Flow deste projecto

- Download -> `git clone https://github.com/maycarlos/password_gen`
- Pode-se tornar o ficheiro interface_click executável com `chmod +x` ou usá-lo da seguinte forma `python interface_click [comando]`

## Mais umas coisinhas para fazer

- [x] Perguntar onde é que esta pass vai ser utilizada e adicionar esta informação no output da da função.  
- [x] Aprender e guardar as passwords num ficheiro JSON(ou outro tipo de ficheiro lindo onde se possa guardar informação) acompanhadas com o ~user~, sítio onde é utilizada e claro ~a password~ encriptada(maybe?).  
- [X] Quero criar um menu para usar na command line. Usei click e o simple term menu que fez tudo o que eu queria do curses por isso vou utliliza-lo para o resto deste projeto  ~(o módulo curses parece ser bom para isso)~  
- [x] Fazer todo o processo reverso quando quiser consultar as passwords quardadas.  
- [x] Começar a ver e trabalhar com databases (sqlite3 parece ser uma coisinha fixe para aprender alguma coisa de SQL).  
