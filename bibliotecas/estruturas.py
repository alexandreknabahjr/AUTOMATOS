# Módulo que contém as constantes que representam as falas do Robô Educativo:
from bibliotecas.falas import *

# Lista dos símbolos válidos na Linguagem do Robô Educativo
ALFABETO = ['mn', 'ci', 'pl', 'di', 'ex', 's', 'n', 'pp', 'vc', 'ma', 'nu', 'ta', 'qu', 'le', 'tr', 'hi', 'pr', 'ds', 'co', 'dl']
# Fim é setado para False (facilita o laço de interação)
eof = False 

# Gera um robô
def robo_topicos():
    robot = {
        pl: 0,
        di: 0,
        pp: 0,
        nu: 0,
        ta: 0,
        qu: 0,
        tr: 0,
        hi: 0,
        ds: 0,
        co: 0,
    }
    return robot

# Zera o robô. Esse dicionário é utilizado sempre que uma palavra é rejeitada pela Linguagem do Robô Educativo
ROBO = {
    pl: 0,
    di: 0,
    pp: 0,
    nu: 0,
    ta: 0,
    qu: 0,
    tr: 0,
    hi: 0,
    ds: 0,
    co: 0,
    }
