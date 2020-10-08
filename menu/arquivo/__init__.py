# ======== ARQUIVO ======== #

def find_file(nome='FILE'):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def new_file(nome_arquivo='FILE'):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('Erro ao criar o arquivo!')
    else:
        print('Arquivo criado.')


def white_file(nome_arquivo='FILE', valor=0):
    try:
        arquivo = open(nome_arquivo, 'w')
    except:
        print(f'Erro ao abrir o arquivo')
    else:
        try:
            arquivo.write(f'{valor}')
        except:
            print('Erro ao gravar dado no arquivo')
        else:
            print('Dado salvo')
    finally:
        arquivo.close()


def read_file(nome_arquivo, nickname):
    with open(nome_arquivo) as nickname:
        leitura = nickname.read()
    print(leitura)
