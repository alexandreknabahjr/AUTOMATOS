# Módulos criados:

# a) Lista que contém o alfabeto; função de geração de um robô; dicionário de tópicos:
from bibliotecas.estruturas import *
# b) Constantes que representam as falas do Robô Educativo:
from bibliotecas.falas import *
# c) Função de transição do Robô Educativo: 
from bibliotecas.robo import *

# inicializacao_robo: Robô -> Robô
# Objetivo: dado um Robô como entrada,
# zera todos os tópicos aprendidos pela criança (usuário)

def inicializacao_robo(robo):
    robo = ROBO
    return robo


# aprendizado: String Robô -> Robô
# Objetivo: dado um tópico aprendido e um Robô,
# retorna a estrutura atualizada correspondente aos tópicos
# aprendidos pela criança (usuário)

def aprendizado(topico, robo):
    robo[topico] += 1
    return robo


# imprime_aprendizado: Robo -> String
# Objetivo: dado um Robô, imprime 
# os tópicos gravados, os quais foram aprendidos
# pela criança (usuário)

def imprime_aprendizado(robo):
    print("\nTópicos aprendidos: ")
    for topico in robo:
        if robo[topico] > 0:
            print(topico, robo[topico])


# erro_padrao: Estado -> String
# Objetivo: dado um movimento inválido, 
# retorna uma mensagem de erro

def erro_padrao(estado = ''):
    print("Zap! Zap! Cuidado! Esse símbolo não pode ser utilizado no momento!")


# le_arquivo: String -> Lista
# Objetivo: dada uma string que representa o nome
# do arquivo de entrada (no padrão CSV), retorna
# uma lista com o seu conteúdo

def le_arquivo(file):

    # Estrutura auxiliar
    with open(file, 'r') as arquivo_entrada:
        conteudo = arquivo_entrada.readlines()
    
    # Lista vazia
    entrada_automatica = []

    # Coloca os símbolos na lista
    for linha in conteudo:
        simbolos = linha.strip().split(',')
        entrada_automatica.extend(simbolos)
    
    # Retorno da lista
    return entrada_automatica