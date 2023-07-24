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
    palavra_escondida = []
    for letra in item_aleatorio:
        palavra_escondida.append('_')
    return palavra_escondida

def exibir_palavra(palavra_escondida):
    print(f'A palavra secreta é a palavra:\n{palavra_escondida}')

# Laço de repetição do programa
def programa_forca(lista):
    limpar_console()
    item_aleatorio = obter_palavra_aleatoria(lista)
    palavra_escondida = esconder_palavra(item_aleatorio)
    letras_usadas = []
    lista_erros = []
    continuar = True
    while continuar == True:
        imprimir_forca(lista_erros)
        exibir_palavra(palavra_escondida)
        print(item_aleatorio)
        letra_escolhida = perguntar_letra()
        limpar_console()
        testar_letra(letra_escolhida, item_aleatorio, letras_usadas, palavra_escondida, lista_erros)
        continuar = tela_de_vitoria(palavra_escondida, item_aleatorio, continuar)
        if continuar == False:
            break
        continuar = game_over(item_aleatorio, lista_erros, continuar)

# Receber tentativa de acerto
def perguntar_letra():
    letra_escolhida = input('Escolha uma letra aleatoria: ').lower()
    return letra_escolhida

# Testar a letra escolhida pelo usuaria
def testar_letra(letra_escolhida, item_aleatorio, letras_usadas, palavra_escondida, lista_erros):
    if letra_escolhida in letras_usadas:
        print(f'A palavra {letra_escolhida} já foi usada anteriormente, escolha novamente')
    elif letra_escolhida in item_aleatorio.lower():
        escolha_certa(letras_usadas, letra_escolhida, item_aleatorio, palavra_escondida)
        return letras_usadas, palavra_escondida
    else:
        lista_erros.append(letra_escolhida)
        escolha_errada(letra_escolhida, letras_usadas, lista_erros)
        return letras_usadas, lista_erros

# Em caso de escolha certa
def escolha_certa(letras_usadas, letra_escolhida, item_aleatorio, palavra_escondida):
    letras_usadas.append(letra_escolhida)
    for index, item in enumerate(item_aleatorio):
        if item == letra_escolhida:
            palavra_escondida[index] = item
    return letras_usadas, palavra_escondida

# Em caso de escolha errada
def escolha_errada(letra_escolhida, letras_usadas, lista_erros):
    letras_usadas.append(letra_escolhida)
    print(f'Voce errou, a palavra secreta não possui a letra {letra_escolhida}')
    print(f'As palavras que voce errou foram: {lista_erros}')
    return(letras_usadas)

# Imprimir a forca no console
def imprimir_forca(lista_erros):
    if len(lista_erros) == 0:
        print(erro_0)
    elif len(lista_erros) == 1:
        print(erro_1)
    elif len(lista_erros) == 2:
        print(erro_2)
    elif len(lista_erros) == 3:
        print(erro_3)
    elif len(lista_erros) == 4:
        print(erro_4)
    elif len(lista_erros) == 5:
        print(erro_5)      

# Tela de vitoria
def tela_de_vitoria(palavra_escondida, item_aleatorio, continuar):
    if '_' not in palavra_escondida:
        print(f'Voce ganhou! a palavra secreta era {item_aleatorio}')
        continuar = False
    else:
        continuar = True
    return continuar

# Tela de game over
def game_over(item_aleatorio, lista_erros, continuar):
    if len(lista_erros) == 6:
        print(erro_6)
        print(f'Game over! Voce errou o maximo de 6 tentativas, a palavra certa era {item_aleatorio}')
        continuar = False
    else:
        continuar = True
    return continuar
    
# Tela de tentar novamente
def tentar_novamente():
    continuar = True
    while continuar == True:
        tentar_novamente_escolha = input('Deseja tentar novamente? ')
        if tentar_novamente_escolha.lower() in ['sim', 's', 'yes', 'y']:
            programa_forca(lista)
        elif tentar_novamente_escolha.lower() in ['não', 'n', 'nao', 'no']:
            print(f'Fechando o programa...')
            break
        else:
            print(f'Opção invalida. Foi inserido "{tentar_novamente_escolha}", escolha entre [sim, s, yes, y] para jogar novamente ou [não, nao, n, no] para fechar o programa')

# Funcao de limpar o console
def limpar_console():
    os.system('cls')

# Codigo principal
lista_txt = obter_lista_txt()
lista = transformar_lista(lista_txt)

programa_forca(lista)
tentar_novamente()
