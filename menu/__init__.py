# ======== MENU ======== #

def linha(tamanho):
    return f'{"-"*tamanho}'


def titulo(msg='TÍTULO', formatacao=0):
    print(f'{linha(formatacao)}'
          f'\n{msg:^{formatacao}}'.upper(),
          f'\n{linha(formatacao)}')


def descritivo(msg):
    print(f'{msg:<}')
