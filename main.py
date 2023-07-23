import random
import os

# Visual da forca
erro_0 = """
   |-------
   |      |
   |
   |
   |
   |
   |
___|___
"""
erro_1 = """
   |-------
   |      |
   |      _
   |     |_|
   |
   |
   |
___|___
"""

erro_2 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |      |
   |      |
   |
___|___
""")

erro_3 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|
   |      |
   |
___|___
""")

erro_4 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |
___|___
""")

erro_5 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     /
___|___
""")

erro_6 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / \\
___|___
""")

# Funções
# Obter a lista do arquivo frutas.txt
def obter_lista_txt():
    lista_txt = open('frutas.txt', 'r')
    return lista_txt

# Tranformar a lista txt em uma lista python
def transformar_lista(lista_txt):
    lista = []
    for item in lista_txt:
        lista.append(item.strip())
    return lista

# Obter um item aleatorio da lista
def obter_palavra_aleatoria(lista):
    item_aleatorio = random.choice(lista)
    return item_aleatorio

# Exibir palavra
def esconder_palavra(item_aleatorio):
    palavra_escondida = ''
    for letra in item_aleatorio:
        palavra_escondida.append('_')
    return palavra_escondida

def exibir_palavra(palavra_escondida):
    print(f'A palavra secreta é a palavra:\n{palavra_escondida}')

# Laço de repetição do programa
def programa_forca(lista):
    obter_palavra_aleatoria(lista)
    letras_usadas = []
    continuar = True
    while continuar == True:
        perguntar_letra()
        testar_letra()
        resultado_parcial()
        imprimir_forca()

# Receber tentativa de acerto
def perguntar_letra():
    letra_escolhida = input('Escolha uma letra aleatoria: ').lower()
    return letra_escolhida

# Testar a letra escolhida pelo usuaria
def testar_letra(letra_escolhida, item_aleatorio, letras_usadas):
    if item_aleatorio in letra_escolhida:
        pass
    if item_aleatorio in letras_usadas:
        print(f'A palavra {letra_escolhida} já foi usada anteriormente, escolha novamente')
    else:
        escolha_errada()

# Em caso de escolha errada
def escolha_errada(erros, letra_escolhida, letras_usadas):
    erros += 1
    letras_usadas.append(letra_escolhida)
    print(f'Voce errou, a palavra secreta não possui a letra {letra_escolhida}')
    resultado_parcial(erros)
    return(letras_usadas)

# Resultado parcial
def resultado_parcial(erros):
    if erros == 6:
        game_over()

# Imprimir a forca no console
def imprimir_forca(erros):
    limpar_console()
    if erros == 0:
        print(erro_0)
    elif erros == 1:
        print(erro_1)
    elif erros == 2:
        print(erro_2)
    elif erros == 3:
        print(erro_3)
    elif erros == 4:
        print(erro_4)
    elif erros == 5:
        print(erro_5)
    else:
        print(erro_6)

def game_over(item_aleatorio):
    print(f'Voce errou o numero maiximo de tentativas, a palavra certa era {item_aleatorio}')
    tentar_novamente()

def tentar_novamente(continuar):
    while continuar == True:
        tentar_novamente_escolha = input('Deseja tentar novamente? ')
        if tentar_novamente_escolha.lower() in ['sim', 's', 'yes', 'y']:
            return programa_forca()
        elif tentar_novamente_escolha.lower() in ['não', 'n', 'nao', 'no']:
            print(f'Fechando o programa...')
            continuar = False
            return continuar
        else:
            print(f'Opção invalida. Foi inserido "{tentar_novamente_escolha}", escolha entre [sim, s, yes, y] para jogar novamente ou [não, nao, n, no] para fechar o programa')
            return tentar_novamente()

def limpar_console():
    os.system('cls')

# Codigo
erros = 0

obter_lista_txt()
transformar_lista()

programa_forca()
