# Módulo criado:

# Funções de interação (interação real ou automática)
from bibliotecas.interacoes import *

def main():
    while True:
        print("Escolha uma opção:")
        print("1 - Interação real")
        print("2 - Interação automática")

        comando = input("\nDigite o número da opção: ")

        if comando == "1":
            # Chamada da função interacao_real()
            interacao_real()
            break
        elif comando == "2":
            # Chamada da função interacao_automatica()
            interacao_automatica()        
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Chamada da função main
if __name__ == "__main__":
    main()
