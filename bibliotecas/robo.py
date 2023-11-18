# Módulo que implementa geradores (pseudo)aleatórios
import random

# Módulos criados:

# a) Funções que alteram o Robo; função de mensagem de erro; função de leitura de arquivo:
from bibliotecas.utils import *
# b) Constantes que representam as falas do Robô Educativo:
from bibliotecas.falas import *
# c) Lista que contém o alfabeto; função de geração de um robô; dicionário de tópicos:
from bibliotecas.estruturas import *


# transicoes: String String Robô -> String Robô Booleano

# Objetivo: esta função retorna o estado atual, os tópicos aprendidos pela criança
# ao utilizar o Robô Educativo e um booleano, o qual representa a aceitação (ou não)
# da palavra de entrada. 

# Exemplos:
    ## a) transicoes ('ma','ta', robot = {
                                #pl: 0,
                                #di: 0,
                                #pp: 0,
                                #nu: 0,
                                #ta: 0,
                                #qu: 0,
                                #tr: 0,
                                #hi: 0,
                                #ds: 0,
                                #co: 0,
                                #})
    ## retornará:
    ## 'ma',  robot = {                     , False
                                #pl: 0,
                                #di: 0,
                                #pp: 0,
                                #nu: 0,
                                #ta: 1,
                                #qu: 0,
                                #tr: 0,
                                #hi: 0,
                                #ds: 0,
                                #co: 0,
                                #})
    ## Neste exemplo, a função retornará False porque é o PADRÃO. 
    ## Só sera retornado True quando a palavra for ACEITA pela Linguagem do Robô
    ## Educativo, isto é, quando o estado for igual a dl (desligamento do robô)
    ## e o booleano correspondente à aceitação for igual a True

    ## b) transicoes ('ci','oi', robot = {
                                #pl: 0,
                                #di: 0,
                                #pp: 0,
                                #nu: 0,
                                #ta: 1,
                                #qu: 0,
                                #tr: 0,
                                #hi: 3,
                                #ds: 0,
                                #co: 0,
                                #})
    ## retornará:
    ## 'liga_robo',  robot = {                     , False
                                #pl: 0,
                                #di: 0,
                                #pp: 0,
                                #nu: 0,
                                #ta: 1,
                                #qu: 0,
                                #tr: 0,
                                #hi: 0,
                                #ds: 0,
                                #co: 0,
                                #})

    ## Neste exemplo, a função retornará False porque é o 
    ## o movimento digitado é INVÁLIDO. 'oi' NÃO existe 
    # na Linguagem do Robô Educativo. Nesse sentido, todos os tópicos
    ## aprendidos são ZERADOS.

# Observação: O autômato que representa essas transições foi discutido
# na Primeira Etapa do Trabalho Final da disciplina.
def transicoes(movimento, estado, robo):
    aceitacao = False

    # Se o movimento escolhido pelo usuário (ou o movimento presente em um arquivo .txt),
    # não estiver na lista:
    # ALFABETO = ['mn', 'ci', 'pl', 'di', 'ex', 's', 'n', 'pp', 'vc', 'ma', 'nu', 'ta', 'qu', 'le', 'tr', 'hi', 'pr', 'ds', 'co', 'dl']
    if not movimento in ALFABETO:

        print("Cuidado! Esse símbolo não pertence ao alfabeto!")
        # Volta para o início
        estado = 'liga_robo'
        # Final
        eof = True
        # A palavra de entrada não é aceita
        aceitacao = False
        # Retorno do estado atual, neste caso, o inicial, retorno 
        # do robô e do booleano referente à aceitação (ou não) da palavra
        return estado, robo, aceitacao

    # Se o estado atual for 'mn' (refere-se ao Menu Principal),
    # e o movimento escolhido for dl, vai para o estado de aceitação do autômato
    if movimento == 'dl' and estado == 'mn':
        print("Beep-bop! Que pena que você me desligou!")
        # Volta para o início
        estado = 'liga_robo'
        # Impressão dos tópicos aprendidos pela criança
        imprime_aprendizado(robo)
        # A palavra de entrada é aceita
        aceitacao = True
        # Retorno do estado atual, neste caso, o inicial, retorno 
        # do robô e do booleano referente à aceitação (ou não) da palavra
        return estado, robo, aceitacao

    if estado == 'liga_robo':

        # Se o estado atual for 'liga_robo' (início do autômato)
        # e o movimento for igual a 'mn', vai para o Menu Principal
        if movimento == 'mn':
            print("Beep! Oi, amigo! Que bom que te ver novamente!")
            estado = 'mn'
        # Caso contrário,
        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao
        
    elif estado == 'mn':

        # Se o estado atual for 'mn' (Menu Principal) e o movimento 
        # escolhido for 'ma' (Menu de Matemática)
        if movimento == 'ma':
            # Impressão dos movimentos possíveis no Menu de Matemática
            print("Beep! Seja bem-vindo ao Menu de Matemática!\n")
            print("nu: Números") 
            print("ta: Tabuada")
            print("qu: Quiz sobre Multiplicação")
            print("mn: Retorno ao Menu Principal")
            # Atualização do estado atual para 'ma'
            estado = 'ma'

        # Se o estado atual for 'mn' (Menu Principal) e o movimento
        # escolhido for 'le' (Menu de Leituras)
        elif movimento == 'le':
            # Impressão dos movimentos possíveis no Menu de Leituras
            print("Beep! Seja bem-vindo ao Menu de Leituras!\n")
            print("tr: Trava-línguas") 
            print("hi: História Infantil")
            # Atualização do estado atual para 'le'
            estado = 'le'

        # Se o estado atual for 'mn' (Menu Principal) e o movimento
        # escolhido for 'pr' (Menu de Programação)
        elif movimento == 'pr':
            # Impressão dos movimentos possíveis no Menu de Programação
            print("Beep! Seja bem-vindo ao Menu de Programação!\n")
            print("ds: Desafio em Scratch") 
            print("co: Conceitos de Programação")
            # Atualização do estado atual para 'pr'
            estado = 'pr'

        # Se o estado atual for 'mn' (Menu Principal) e o movimento
        # escolhido for 'ci' (Menu de Ciências)       
        elif movimento == 'ci':
            # Impressão dos movimentos possíveis no Menu de Ciências
            print("Beep! Seja bem-vindo ao Menu de Ciências!\n")
            print("pl: Planetas") 
            print("di: Dinossauros")
            print("ex: Menu de Experimento Simples")
            # Atualização do estado atual para 'ci'
            estado = 'ci'

        # Caso contrário,
        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'ma':
        # Se estado atual for 'ma' (Menu de Matemática) e o movimento escolhido
        # for 'nu', acessa as curiosidades sobre os números
        if movimento == 'nu':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de curiosidades no Robô Educativo
            if randomico == 1:
                print(NU1)
            if randomico == 2:
                print(NU2)
            if randomico == 3:
                print(NU3)
            # Grava o tópico aprendido
            robo = aprendizado(nu, robo)

        # Se estado atual for 'ma' (Menu de Matemática) e o movimento escolhido
        # for 'ta', acessa a tabuada
        elif movimento == 'ta':
            # Impressão da tabela completa
            for numero in range(1, 11):
                print(f"Tabuada do {numero}:")
                for i in range(1, 11):
                    resultado = numero * i
                    print(f"{numero} x {i} = {resultado}")
                print()
            # Grava o tópico aprendido
            robo = aprendizado(ta, robo)

        # Se estado atual for 'ma' (Menu de Matemática) e o movimento escolhido
        # for 'qu', acessa o quiz sobre multiplicação
        elif movimento == 'qu':
            # Geração de números aleatórios
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            print("Quanto é {} x {}?".format(num1, num2))
            # Grava o tópico aprendido
            robo = aprendizado(qu, robo)

        # Se estado atual for 'ma' (Menu de Matemática) e o movimento escolhido
        # for 'mn', volta para o Menu Principal
        elif movimento == 'mn':
            print("Beep! Voltando ao Menu Principal...")
            # Atualização do estado atual para 'mn'
            estado = 'mn'

        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'le':

        # Se estado atual for 'le' (Menu de Leituras) e o movimento escolhido
        # for 'tr', vai para o Trava-línguas
        if movimento == 'tr':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de trava-línguas no Robô Educativo
            if randomico == 1:
                print(TR1)
            if randomico == 2:
                print(TR2)
            if randomico == 3:
                print(TR3)
            # Grava o tópico aprendido
            robo = aprendizado(tr, robo)

        # Se estado atual for 'hi' (Menu de Leituras) e o movimento escolhido
        # for 'hi', vai para a história infantil curta
        elif movimento == 'hi':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de histórias infantis curtas no Robô Educativo
            if randomico == 1:
                print(HI1)
            if randomico == 2:
                print(HI2)
            if randomico == 3:
                print(HI3)
            # Gravação do tópico aprendido
            robo = aprendizado(hi, robo)

        # Se estado atual for 'le' (Menu de Leituras) e o movimento escolhido
        # for 'mn', volta para o Menu Principal
        elif movimento == 'mn':
            print("Beep! Voltando ao Menu Principal...")
            # Atualização do estado para 'mn'
            estado = 'mn'

        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'pr':

        # Se estado atual for 'pr' (Menu de Programação) e o movimento escolhido
        # for 'ds', vai para o desafio em Scratch
        if movimento == 'ds':
            # Geração de um número aleatório
            randomico = random.randint(1, 2)
            # Existem duas opções de desafios em Scratch no Robô Educativo
            if randomico == 1:
                print(DS1)
            if randomico == 2:
                print(DS2)
            # Gravação do tópico aprendido
            robo = aprendizado(ds, robo)

        # Se estado atual for 'pr' (Menu de Programação) e o movimento escolhido
        # for 'co', vai para os conceitos de programação
        elif movimento == 'co':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de conceitos de programação no Robô Educativo
            if randomico == 1:
                print(CO1)
            if randomico == 2:
                print(CO2)
            if randomico == 3:
                print(CO3)
            # Gravação do tópico aprendido
            robo = aprendizado(co, robo)

        # Se estado atual for 'pr' (Menu de Programação) e o movimento escolhido
        # for 'mn', volta para o Menu Principal
        elif movimento == 'mn':
            print("Beep! Voltando ao Menu Principal...")
            # Atualização para o estado 'mn'
            estado = 'mn'

        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'ci':

        # Se estado atual for 'ci' (Menu de Ciências) e o movimento escolhido
        # for 'pl', vai para as curiosidades sobre planetas
        if movimento == 'pl':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de curiosidades sobre planetas no Robô Educativo
            if randomico == 1:
                print(PL1)
            if randomico == 2:
                print(PL2)
            if randomico == 3:
                print(PL3)
            # Gravação do tópico aprendido
            robo = aprendizado(pl, robo)

        # Se estado atual for 'ci' (Menu de Ciências) e o movimento escolhido
        # for 'di', vai para as curiosidades sobre dinossauros
        elif movimento == 'di':
            # Geração de um número aleatório
            randomico = random.randint(1, 3)
            # Existem três opções de curiosidades sobre dinossauros no Robô Educativo
            if randomico == 1:
                print(DI1)
            if randomico == 2:
                print(DI2)
            if randomico == 3:
                print(DI3)
            # Gravação do tópico aprendido
            robo = aprendizado(di, robo)

        # Se estado atual for 'ci' (Menu de Ciências) e o movimento escolhido
        # for 'ex', vai para o Menu de Experimento Simples
        elif movimento == 'ex':
            print("Zaz! Que legal! Vamos fazer um experimento juntos?")
            # Atualização do estado para 'ex'
            estado = 'ex'

        # Se estado atual for 'ci' (Menu de Ciências) e o movimento escolhido
        # for 'mn', volta para o Menu Principal
        elif movimento == 'mn':
            print("Beep! Voltando ao Menu Principal...")
            # Atualização do estado para 'mn'
            estado = 'mn'

        # Caso contrário
        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'ex':

        # Se estado atual for 'ex' (Menu de Experimento Simples) e o movimento escolhido
        # for 's', é possível acessar o experimento
        if movimento == 's':
            print("Iubeep! Que bom que seus pais estão por perto!")
            # Atualização para o estado 'pp'
            estado = 'pp'

        # Se estado atual for 'ex' (Menu de Experimento Simples) e o movimento escolhido
        # for 'n', volta para o Menu de Ciências
        elif movimento == 'n':
            print("Zzzzz... Que pena que os seus pais não estão por aqui... Tente novamente mais tarde!")
            # Atualização para o estado 'ci'
            estado = 'ci'

        # Caso contrário,
        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é a ceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    elif estado == 'pp':
        # Se o estado atual for 'pp' (Experimento Simples)
        # e o movimento escolhido for o próprio 'pp'
        if movimento == 'pp':
            # Geração de um número aleatório
            randomico = random.randint(1, 2)
            # Existem três opções de experimentos no Robô Educativo
            if randomico == 1:
                print(PP1)
            if randomico == 2:
                print(PP2)
            # Grava o tópico aprendido
            robo = aprendizado(pp, robo)

        # Se o estado atual for 'pp' (Experimento Simples)
        # e o movimento escolhido for 'vc', o Robô Educativo
        # volta para o Menu de Ciências
        elif movimento == 'vc':
            print("Zup! Voltando ao Menu de Ciências...")
            # Atualização do estado para 'ci'
            estado = 'ci'

        # Caso contrário,
        else:
            # Exibição da mensagem de erro
            erro_padrao(estado)
            # Volta para o início
            estado = 'liga_robo'
            # A palavra não é aceita
            aceitacao = False
            # Função que zera os tópicos aprendidos
            robo = inicializacao_robo(robo)
            # Retorno do estado atual, neste caso, o inicial, retorno 
            # do robô e do booleano referente à aceitação (ou não) da palavra
            return estado, robo, aceitacao

    # Garantia de retorno
    return estado, robo, aceitacao