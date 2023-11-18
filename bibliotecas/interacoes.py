# Módulos criados:

# a) Função de transição do Robô Educativo: 
from bibliotecas.robo import *
# b) Funções que alteram o Robo; função de mensagem de erro; função de leitura de arquivo:
from bibliotecas.utils import *
# c) Lista que contém o alfabeto; função de geração de um robô; dicionário de tópicos:
from bibliotecas.estruturas import *
# d) Constantes que representam as falas do Robô Educativo:
from bibliotecas.falas import *


# interacao_real: Sem entrada -> String
# Objetivo: dados símbolos DIGITADOS pela criança (ou responsável pela criança),
# que, no caso, é o usuário, retorna uma mensagem de aceitação ou rejeição da palavra.

# Observação: O autômato que representa as transições foi discutido
# na Primeira Etapa do Trabalho Final da disciplina.

def interacao_real():

    # Chamada da função robo_topicos()
    robo_aux = robo_topicos()
    # Etado inicial
    estado = 'liga_robo'
    # A aceitação PADRÃO é False
    aceitacao = False
    while not eof:
        print("Estado atual: ", estado)
        movimento = input("Digite uma transição: ")
        print("\n")
        # Se o movimento não for vazio
        if movimento == "":
            # Se a aceitação for igual a True
            if aceitacao:
                print("\nBeep! Beep! A palavra foi aceita!")
            # Caso contrário,
            else:
                print("\nTzzzzz... Sou um robô em fase de planejamento! A palavra de entrada foi rejeitada!")
        
            saida = input("Deseja sair? (S - Sim): ")

            # Se o usuário deseja sair
            if saida == 'S':
                break
        # Atualização do estado atual, do Robô e da aceitação
        estado, robo_aux, aceitacao = transicoes(movimento, estado, robo_aux)
    


# interacao_real: Sem entrada -> String
# Objetivo: dados símbolos em um ARQUIVO, retorna uma mensagem de aceitação ou rejeição da palavra.

# Observação: O autômato que representa as transições foi discutido
# na Primeira Etapa do Trabalho Final da disciplina.

def interacao_automatica():

    # Chamada da função robo_topicos()
    robo_aux = robo_topicos()
    # Etado inicial
    estado = 'liga_robo'
    # Caminho da pasta + / + nomedoarquivo.txt
    nome_arquivo = "testes/" + input("Digite o nome do arquivo de entrada: ")
    # Chamada da função le_arquivo()
    simbolos = le_arquivo(nome_arquivo)
    simbolos.append('')
    for movimento in simbolos:
        print("Transição: ", movimento)
        # Se o movimento não for vazio
        if movimento == "":
            # Se a aceitação for igual a True
            if aceitacao:
                print("\nBeep! Beep! A palavra foi aceita!")
            # Caso contrário,
            else:
                print("\nTzzzzz... Sou um robô em fase de planejamento! A palavra de entrada foi rejeitada!")
        
            saida = input("Deseja sair? (S - Sim): ")

            # Se o usuário deseja sair
            if saida == 'S':
                break
        # Atualização do estado atual, do Robô e da aceitação
        estado, robo_aux, aceitacao = transicoes(movimento, estado, robo_aux)

