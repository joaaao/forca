#O comando "import random" é utilizado para importar uma biblioteca para escolher aleatoriamente.
import random
#Variavel criada para ser a lista que contém as palavras que poderão estar contidas no jogo 
palavras = ['abacate','chocolate','paralelepipedo','goiaba']
#Variavel responsável para mostrar as letras que não esta contida nas palavras 
letrasErradas = ''
#Variavel responsável para mostrar as letras que esta contida nas palavras 
letrasCertas = ''
#variavel para criar o especto fisico do jogo
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#O comando "def principal" é responsavel por comandar as principais funções do jogo
def principal():
    """
    Função Princial do programa
    """
#O comando "print" é responsavel por imprimir algo na tela    
     print('F O R C A')
#Variavel que tem a função de escolher aleatoriamente a palavra que será usada no jogo 
    palavraSecreta = sortearPalavra()
#Variavel usada para ser a letra que o jogador palpitou
    palpite = ''
#Variavel responsavel para julgar a letra que o jogador digitou está certa ou errada     
    desenhaJogo(palavraSecreta,palpite)
#Comando utilizado para repetir a função enquanto a sentença for verdadeira 
    while True:
#Variavel que vai receber a letra que o jogador digitou         
        palpite = receberPalpite()
#Variavel que vai julgar o palpite do jogador 
        desenhaJogo(palavraSecreta,palpite)
#Comando que sera utiliado para verificar se a sentença é verdadeira ou não. Caso for verdadeira o comando entra em ação. 
        if perdeuJogo():
#O comando "print" é responsavel por imprimir algo na tela
            print('Voce Perdeu!!!')
#Comado utilizado para parar o comando if
            break
#Comando que sera utiliado para verificar se a sentença é verdadeira ou não. Caso for verdadeira o comando entra em ação. 
        if ganhouJogo(palavraSecreta):
#O comando "print" é responsavel por imprimir algo na tela
            print('Voce Ganhou!!!')
#Comado utilizado para parar o comando if
            break            
#O comando "def perdeuJogo" é responsavel por comandar as funções caso o jogador perca o jogo        
def perdeuJogo():
#O comando "global" serve para colocar a variavel "FORCAIMG" em cena mesmo que o camando "def perdeuJogo" não seja acionado.
    global FORCAIMG
#testa se a variavel "letrasErrada" tem o mesmo peso que a variavel "FORCAIMG".
    if len(letrasErradas) == len(FORCAIMG):
#Caso o comando "def perdeuJogo" seja ativado, o "return True" sera verdade. Caso contrario o comando sera falso.
        return True
#Comando utilizado para caso o comando "if" nao seja ativado.
    else:
#Caso o comando "def perdeuJogo" seja ativado, o "return False" sera verdade. Caso contrario o comando sera falso.
        return False
#Comando utilizado pare "entrar em cena" caso o jogador vença.    
def ganhouJogo(palavraSecreta):
#O comando "global" serve para colocar a variavel "letrasCertas" em cena mesmo que a "def ganhouJogo" não seja acionado. Fezendo com que ela seja global. 
    global letrasCertas
#Variavel utilizada para comprovar que o jogador ganhou o jogo 
    ganhou = True
#comando utilizado para verificar se a letra esta ou nao contida na palavra.
    for letra in palavraSecreta:
#Caso nao esteja contido, este comando sera utilizado         
        if letra not in letrasCertas:
#Caso nao esteja, o jogador não tera ganho o jogo 
            ganhou = False
#Comando utilizado para voltar na variavel "ganhou"
    return ganhou        
        

#Comando utilizado para testar o palpite do jogador 
def receberPalpite():
#Variavel utilizada para "pedir" uma letra para o jogador    
    palpite = input("Adivinhe uma letra: ")
#Variavel para dixar tudo em maiusculo
    palpite = palpite.upper()
#Comando utilizado para verificar se o jogador escreveu apenas uma letra
    if len(palpite) != 1:
#O comando "print" é responsavel por imprimir algo na tela
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
#O comando "print" é responsavel por imprimir algo na tela
        print('Voce ja disse esta letra.')
#Comando utilizado para testar se o jogador esta escrevendo apenas letras
    elif not "A" <= palpite <= "Z":
#O comando "print" é responsavel por imprimir algo na tela
        print('Por favor escolha apenas letras')
#Comando utilizado para caso o comando "if" nao seja ativado.
    else:
#Comando utilizado para voltar na variavel "palpite"
        return palpite
    
#Comando utilizado para organizado o jogo em uma ordem para que o jogador consiga entender o jogo com facilidade     
def desenhaJogo(palavraSecreta,palpite):
#Vai fazer com que esta variavel se torne global 
    global letrasCertas
#Vai fazer com que esta variavel se torne global
    global letrasErradas
#Vai fazer com que esta variavel se torne global
    global FORCAIMG
#O comando "print" é responsavel por imprimir algo na tela
    print(FORCAIMG[len(letrasErradas)])
    
#Variavel criada para cria '-' na palavra certa     
    vazio = len(palavraSecreta)*'-'
#Se a letra que o jogador digitou está contidada na palavra secreta, adicione uma letra a "letrasCertas".    
    if palpite in palavraSecreta:
        letrasCertas += palpite
#Caso a letra não esteja contida, a letra inserida pelo jogador vai ser adicionada a "letrasErradas".
    else:
        letrasErradas += palpite
#Caso a letra esteja inserida em letra certa.
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
#O comando "print" neste caso responsavel por imprimir os acertos na tela                
    print('Acertos: ',letrasCertas )
#O comando "print" neste caso responsavel por imprimir os erros na tela
    print('Erros: ',letrasErradas)
    print(vazio)
     
#Comando responsável por escolher uma palavra randomicamente para o jogo.
def sortearPalavra():
#Torna a variável "palavras" global.
    global palavras
#Comando utilizado para voltar na variável "palavras". E o ".upper" serve para corrigir a escrita do jogador.
    return random.choice(palavras).upper()

    
principal()
