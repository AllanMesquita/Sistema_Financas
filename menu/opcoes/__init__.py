# ======== OPÇÕES ======== #

def opcoes(lista):
    contador = 1
    for i in lista:
        print(f'{contador:>2} - {i}')
        contador += 1


def input_usuario(msg):
    while True:
        try:
            usuario = int(input(f'{msg}'))
        except:
            print(f'\033[31mValor inválido. '
                  f'\nSomente números inteiros são aceitos.'
                  f'\nTente novamente\033[m')
        else:
            return usuario


def input_dado_usuario(msg='TEXTO'):
    usuario = float(input(msg))
    return usuario


def input_comum(msg='TEXTO'):
    usuario = input(msg)
    return usuario

