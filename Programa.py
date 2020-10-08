# ======== SISTEMA DE FINANÇAS ======= #

import menu.opcoes
from menu import arquivo

# CABEÇALHO
menu.titulo('SISTEMA de FINANÇAS', 60)
menu.descritivo('\nPrograma básico para organização financeira.')
print(f'\n{menu.linha(60)}')

print()

# BLOCO -ENTRADA DE DADOS-

while True:
    titulo = 'MENU PRINCIPAL'

    print(menu.linha(60))

    menu.titulo(titulo, len(titulo))

    print()

    menu.opcoes.opcoes(['ENTRADA DE DADOS'])

    usuario = menu.opcoes.input_usuario('>>> ')

    if usuario > 1:
        print(f'{"Opção inválida":^60}'
              f'\n{"Tente novamente":^60}')
        continue

    # BLOCO -RECEITA E DESPESAS-

    if usuario == 1:
        while True:
            print(menu.linha(60))

            menu.opcoes.opcoes(['RECEITA',
                                'DESPESAS'])

            usuario = menu.opcoes.input_usuario('>>> ')

            if usuario > 2:
                print(f'{"Opção inválida":^60}'
                      f'\n{"Tente novamente":^60}')
                continue

            # BLOCO - RECEITA -

            if usuario == 1:

                titulo = 'RECEITA'

                print(menu.linha(60))

                while True:

                    menu.titulo(titulo, len(titulo))

                    menu.opcoes.opcoes(['SALÁRIO',
                                        'BÔNUS/EXTRAS',
                                        'FÉRIAS',
                                        '13º SALÁRIO'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    if usuario > 4:
                        print(f''
                              f'\n{"Opção inválida":^60}'
                              f'\n{"Tente novamente":^60}'
                              f'\n')

                    # BLOCO -SALÁRIO-

                    if usuario == 1:
                        arquivo_salario = 'arquivo_salario'

                        print(menu.linha(60))

                        if menu.arquivo.find_file(arquivo_salario) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_salario)

                            else:
                                print('Necessário a criação do arquivo para continuar.')
                                break

                        titulo = f'RECEITA' \
                                 f'\nSALÁRIO'

                        print()

                        menu.titulo(titulo, len(titulo) - 8)

                        menu.descritivo('Breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_salario, usuario)

                        menu.arquivo.read_file(arquivo_salario, 'salario')

                    # BLOCO -BÔNUS/EXTRAS-

                    if usuario == 2:
                        arquivo_bonus_extra = 'arquivo_bonus_extras'

                        print(menu.linha(60))

                        if menu.arquivo.find_file(arquivo_bonus_extra) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_bonus_extra)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'RECEITA' \
                                 '\nBÔNUS / EXTRAS'

                        print()

                        menu.titulo(titulo, len(titulo) - 8)

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_bonus_extra, usuario)

                        menu.arquivo.read_file(arquivo_bonus_extra, 'bonusExtra')

                    # BLOCO -FÉRIAS-

                    print(menu.linha(60))

                    if usuario == 3:
                        arquivo_ferias = 'arquivo_ferias'

                        if menu.arquivo.find_file(arquivo_ferias) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_ferias)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'RECEITA - ' \
                                 '\n- FÉRIAS'

                        menu.titulo(titulo, len(titulo) - 10)

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_ferias, usuario)

                        menu.arquivo.read_file(arquivo_ferias, 'ferias')

                    # BLOCO -13 SALÁRIO-

                    if usuario == 4:

                        arquivo_13_salario = 'arquivo_13_salario'

                        if menu.arquivo.find_file(arquivo_13_salario) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_13_salario)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'RECEITA - ' \
                                 '\n- 13º SALÁRIO'

                        menu.titulo(titulo, len(titulo) - 11)

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_13_salario, usuario)

                        menu.arquivo.read_file(arquivo_13_salario, '13_salario')

            # BLOCO -DESPESAS-

            if usuario == 2:

                titulo = 'DESPESAS'

                print(menu.linha(60))

                menu.titulo(titulo, len(titulo))

                menu.opcoes.opcoes(['HABITAÇÃO',
                                    'SAÚDE',
                                    'TRANSPORTE',
                                    'DESPESAS PESSOAIS',
                                    'EDUCAÇÃO',
                                    'TAXAS',
                                    'LAZER',
                                    'VARIÁVEIS'])

                usuario = menu.opcoes.input_usuario('>>> ')

                # BLOCO -HABITAÇÂO-

                if usuario is 1:

                    titulo = 'HABITAÇÃO'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo("Breve explicação")

                    menu.opcoes.opcoes(['ALUGUEL',
                                        'LUZ',
                                        'ÁGUA',
                                        'CELULAR',
                                        'INTERNET',
                                        'STREAMING',
                                        'MERCADO',
                                        'LAVANDERIA',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -HABITAÇÃO-ALUGUEL-

                    if usuario is 1:

                        arquivo_aluguel = 'arquivo_aluguel'

                        if menu.arquivo.find_file(arquivo_aluguel) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_aluguel)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'DESPESAS - ' \
                                 '\n- ALUGUEL'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_aluguel, usuario)

                        menu.arquivo.read_file(arquivo_aluguel, 'aluguel')

                    # BLOCO -HABITAÇÃO-LUZ-

                    if usuario is 2:

                        arquivo_luz = 'arquivo_luz'

                        if menu.arquivo.find_file(arquivo_luz) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_luz)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'LUZ'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_luz, usuario)

                        menu.arquivo.read_file(arquivo_luz, 'luz')

                    # BLOCO -HABITAÇÃO-ÁGUA

                    if usuario is 3:

                        arquivo_agua = 'arquivo_agua'

                        if menu.arquivo.find_file(arquivo_agua) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_agua)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ÁGUA'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_agua, usuario)

                        menu.arquivo.read_file(arquivo_agua, 'agua')

                    # BLOCO -HABITAÇÃO-CELULAR-

                    if usuario is 4:

                        arquivo_celular = 'arquivo_celular'

                        if menu.arquivo.find_file(arquivo_celular) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_celular)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'CELULAR'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_celular, usuario)

                        menu.arquivo.read_file(arquivo_celular, 'celular')

                    # BLOCO -HABITAÇÃO-INTERNET-

                    if usuario is 5:

                        arquivo_internet = 'arquivo_internet'

                        if menu.arquivo.find_file(arquivo_internet) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_internet)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'INTERNET'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_internet, usuario)

                        menu.arquivo.read_file(arquivo_internet, 'internet')

                    # BLOCO -HABITAÇÃO-STREAMING-

                    if usuario is 6:

                        arquivo_streaming = 'arquivo_streaming'

                        if menu.arquivo.find_file(arquivo_streaming) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_streaming)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'STREAMING'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_streaming, usuario)

                        menu.arquivo.read_file(arquivo_streaming, 'streaming')

                    # BLOCO -HABITAÇÃO-MERCADO-

                    if usuario is 7:

                        arquivo_mercado = 'arquivo_mercado'

                        if menu.arquivo.find_file(arquivo_mercado) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_mercado)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MERCADO'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_mercado, usuario)

                        menu.arquivo.read_file(arquivo_mercado, 'mercado')

                    # BLOCO -HABITAÇÃO-LAVANDERIA-

                    if usuario is 8:

                        arquivo_lavanderia = 'arquivo_lavanderia'

                        if menu.arquivo.find_file(arquivo_lavanderia) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_lavanderia)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'LAVANDERIA'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_lavanderia, usuario)

                        menu.arquivo.read_file(arquivo_lavanderia, 'lavanderia')

                    # BLOCO -HABITAÇÃO-OUTROS-

                    if usuario is 9:

                        arquivo_habitacao_outros = 'arquivo_habitacao_outros'

                        if menu.arquivo.find_file(arquivo_habitacao_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_habitacao_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                        menu.descritivo('breve explicação')

                        usuario = menu.opcoes.input_dado_usuario('R$ ')

                        menu.arquivo.white_file(arquivo_habitacao_outros, usuario)

                        menu.arquivo.read_file(arquivo_habitacao_outros, 'habitacao_outros')

                # BLOCO -SAÚDE-

                if usuario is 2:

                    titulo = 'SAÚDE'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo("Breve explicação")

                    menu.opcoes.opcoes(['MEDICAMENTOS',
                                        'DENTISTA',
                                        'MÉDICO',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -SAÚDE-MEDICAMENTOS-

                    if usuario is 1:

                        arquivo_medicamentos = 'arquivo_medicamentos'

                        if menu.arquivo.find_file(arquivo_medicamentos) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_medicamentos)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MEDICAMENTOS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -SAÚDE-DENTISTA-

                    if usuario is 2:

                        arquivo_dentista = 'arquivo_dentista'

                        if menu.arquivo.find_file(arquivo_dentista) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_dentista)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'DENTISTA'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -SAÚDE-MÉDICO-

                    if usuario is 3:

                        arquivo_medico = 'arquivo_medico'

                        if menu.arquivo.find_file(arquivo_medico) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_medico)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MÉDICO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO - SAÚDE-OUTROS-

                    if usuario is 4:

                        arquivo_saude_outros = 'arquivo_saude_outros'

                        if menu.arquivo.find_file(arquivo_saude_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_saude_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -TRANSPORTE-

                if usuario is 3:

                    titulo = 'TRANSPORTE'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo("Breve explicação")

                    menu.opcoes.opcoes(['PASSAGEM',
                                        'TAXI/UBER',
                                        'ALUGUEL CARRO',
                                        'MANUTENÇÃO',
                                        'COMBUSTÍVEL',
                                        'ESTACIONAMENTO',
                                        'LAVAGEM',
                                        'PEDÁGIO',
                                        'MULTAS',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -TRANSPORTE-PASSAGEM- *Achar um nome melhor*

                    if usuario is 1:

                        arquivo_passagem = 'arquivo_passagem'

                        if menu.arquivo.find_file(arquivo_passagem) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_passagem)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'PASSAGEM'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-TAXI/UBER-

                    if usuario is 2:

                        arquivo_taxiuber = 'arquivo_taxiuber'

                        if menu.arquivo.find_file(arquivo_taxiuber) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_taxiuber)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'TAXI/UBER'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-ALUGUEL CARRO-

                    if usuario is 3:

                        arquivo_aluguelcarro = 'arquivo_aluguelcarro'

                        if menu.arquivo.find_file(arquivo_aluguelcarro) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_aluguelcarro)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ALUGUEL CARRO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-MANUTENÇÃO-

                    if usuario is 4:

                        arquivo_manutencao = 'arquivo_manutencao'

                        if menu.arquivo.find_file(arquivo_manutencao) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_manutencao)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MANUTENÇÃO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-COMBUSTÍVEL-

                    if usuario is 5:

                        arquivo_combustivel = 'arquivo_combustivel'

                        if menu.arquivo.find_file(arquivo_combustivel) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_combustivel)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'COMBUSTÍVEL'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-ESTACIONAMENTO-

                    if usuario is 6:

                        arquivo_estacionamento = 'arquivo_estacionamento'

                        if menu.arquivo.find_file(arquivo_estacionamento) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_estacionamento)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ESTACIONAMENTO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-LAVAGEM-

                    if usuario is 7:

                        arquivo_lavagem = 'arquivo_lavagem'

                        if menu.arquivo.find_file(arquivo_lavagem) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_lavagem)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'LAVAGEM'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-PEDÁGIO-

                    if usuario is 8:

                        arquivo_pedagio = 'arquivo_pedagio'

                        if menu.arquivo.find_file(arquivo_pedagio) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_pedagio)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'PEDÁGIO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-MULTAS-

                    if usuario is 9:

                        arquivo_multas = 'arquivo_multas'

                        if menu.arquivo.find_file(arquivo_multas) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_multas)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MULTAS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TRANSPORTE-OUTROS-

                    if usuario is 10:

                        arquivo_transporte_outros = 'arquivo_transporte_outros'

                        if menu.arquivo.find_file(arquivo_transporte_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_transporte_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -DESPESAS PESSOAIS-

                if usuario is 4:

                    titulo = 'DESPESAS PESSOAIS'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo('Breve descrição')

                    menu.opcoes.opcoes(['VESTUÁRIO',
                                        'CABELEIREIRO',
                                        'COSMÉTICOS',
                                        'ACADEMIA',
                                        'ESPORTES',
                                        'SERVIÇOS ESTÉTICOS',
                                        'OUTROS'])

                    menu.opcoes.input_usuario('>>> ')

                    # BLOCO -DESPESAS PESSOAIS-VESTUÁRIO-

                    if usuario is 1:

                        arquivo_vestuario = 'arquivo_vestuario'

                        if menu.arquivo.find_file(arquivo_vestuario) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_vestuario)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'VESTUÁRIO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-CABELEIREIRO-

                    if usuario is 2:

                        arquivo_cabeleireiro = 'arquivo_cabeleireiro'

                        if menu.arquivo.find_file(arquivo_cabeleireiro) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_cabeleireiro)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'CABELEIREIRO'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-COSMÉTICOS-

                    if usuario is 3:

                        arquivo_cosmeticos = 'arquivo_cosmeticos'

                        if menu.arquivo.find_file(arquivo_cosmeticos) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_cosmeticos)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'COSMÉTICOS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-ACADEMIA-

                    if usuario is 4:

                        arquivo_academia = 'arquivo_academia'

                        if menu.arquivo.find_file(arquivo_academia) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_academia)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ACADEMIA'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-ESPORTES-

                    if usuario is 5:

                        arquivo_esportes = 'arquivo_esportes'

                        if menu.arquivo.find_file(arquivo_esportes) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_esportes)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ESPORTES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-SERVIÇOS ESTÉTICOS-

                    if usuario is 6:

                        arquivo_servico_estetico = 'arquivo_servico_estetico'

                        if menu.arquivo.find_file(arquivo_servico_estetico) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_servico_estetico)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'SERVICOS ESTÉTICOS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -DESPESAS PESSOAIS-OUTROS-

                    if usuario is 7:

                        arquivo_despeas_pessoais_outros = 'arquivo_despesas_pessoais_outros'

                        if menu.arquivo.find_file(arquivo_despeas_pessoais_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_despeas_pessoais_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -EDUCAÇÃO-

                if usuario is 5:

                    titulo = 'EDUCAÇÃO'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo('Breve descrição')

                    menu.opcoes.opcoes(['ESCOLA/FACULDADE',
                                        'CURSOS',
                                        'MATERIAL ESCOLAR',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -EDUCAÇÃO-ESCOLA/FACULDADE-

                    if usuario is 1:

                        arquivo_escola_faculdade = 'arquivo_escola_faculdade'

                        if menu.arquivo.find_file(arquivo_escola_faculdade) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_escola_faculdade)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'ESCOLA/FACULDADE'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -EDUCAÇÃO-CURSOS-

                    if usuario is 2:

                        arquivo_cursos = 'arquivo_cursos'

                        if menu.arquivo.find_file(arquivo_cursos) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_cursos)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'CURSOS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -EDUCAÇÃO-MATERIAL ESCOLAR-

                    if usuario is 3:

                        arquivo_material_escolar = 'arquivo_material_escolar'

                        if menu.arquivo.find_file(arquivo_material_escolar) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_material_escolar)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MATERIAL ESCOLAR'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -EDUCAÇÃO-OUTROS

                    if usuario is 4:

                        arquivo_educacao_outros = 'arquivo_educacao_outros'

                        if menu.arquivo.find_file(arquivo_educacao_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_educacao_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -TAXAS-

                if usuario is 6:

                    titulo = 'TAXAS'

                    menu.titulo(titulo, len(titulo))

                    menu.descritivo('Breve explicação')

                    menu.opcoes.opcoes(['TARIAFAS BANCÁRIAS',
                                        'I.R.',
                                        'PENSÕES',
                                        'GORJETAS/CAIXINHA',
                                        'DOAÇÕES',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -TAXAS-TARIFAS BANCÁRIAS-

                    if usuario is 1:

                        arquivo_tarifas = 'arquivo_tarias'

                        if menu.arquivo.find_file(arquivo_tarifas) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_tarifas)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'TARIAFAS BANCÁRIAS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TAXAS-I.R.-

                    if usuario is 2:

                        arquivo_ir = 'arquivo_ir'

                        if menu.arquivo.find_file(arquivo_ir) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_ir)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'I.R.'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TAXAS-PENSÕES-

                    if usuario is 3:

                        arquivo_pensoes = 'arquivo_pensoes'

                        if menu.arquivo.find_file(arquivo_pensoes) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_pensoes)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'PENSÕES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TAXAS-GORJETAS/CAIXINHA-

                    if usuario is 4:

                        arquivo_gorjetas = 'arquivo_gorjetas'

                        if menu.arquivo.find_file(arquivo_gorjetas) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_gorjetas)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'GORJETAS/CAIXINHA'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TAXAS-DOAÇÕES-

                    if usuario is 5:

                        arquivo_doacoes = 'arquivo_doacoes'

                        if menu.arquivo.find_file(arquivo_doacoes) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_doacoes)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'DOAÇÕES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -TAXAS-OUTROS-

                    if usuario is 6:

                        arquivo_taxas_outros = 'arquivo_taxas_outros'

                        if menu.arquivo.find_file(arquivo_taxas_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_taxas_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -LAZER-

                if usuario is 7:

                    titulo = 'LAZER'

                    menu.titulo(titulo, len(titulo))

                    menu.opcoes.opcoes(['BARES/RESTAURANTES',
                                        'SHOW/EVENTOS',
                                        'LIVROS',
                                        'GAMES',
                                        'PASSAGENS',
                                        'HOSPEDAGENS',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -LAZER-BARES/RESTAURANTES-

                    if usuario is 1:

                        arquivo_bares = 'arquivo_bares'

                        if menu.arquivo.find_file(arquivo_bares) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_bares)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'BARES/RESTAURANTES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-SHOW/EVENTOS-

                    if usuario is 2:

                        arquivo_showEventos = 'arquivo_showEventos'

                        if menu.arquivo.find_file(arquivo_showEventos) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_showEventos)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'SHOW/EVENTOS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-LIVROS-

                    if usuario is 3:

                        arquivo_livros = 'arquivo_livros'

                        if menu.arquivo.find_file(arquivo_livros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_livros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'LIVROS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-GAMES-

                    if usuario is 4:

                        arquivo_games = 'arquivo_games'

                        if menu.arquivo.find_file(arquivo_games) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_games)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'GAMES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-PASSAGENS-

                    if usuario is 5:

                        arquivo_passagens = 'arquivo_passagens'

                        if menu.arquivo.find_file(arquivo_passagens) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_passagens)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'PASSAGENS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-HOSPEDAGENS-

                    if usuario is 6:

                        arquivo_hospedagens = 'arquivo_hospedagens'

                        if menu.arquivo.find_file(arquivo_hospedagens) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_hospedagens)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'HOSPEDAGENS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -LAZER-OUTROS-

                    if usuario is 7:

                        arquivo_lazer_outros = 'arquivo_lazer_outros'

                        if menu.arquivo.find_file(arquivo_lazer_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_lazer_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                # BLOCO -VARIÁVEIS-

                if usuario is 8:

                    titulo = f'{"VARIÁVEIS"}'

                    menu.titulo(titulo, len(titulo))

                    menu.opcoes.opcoes(['MANUTENÇÃO/REPAROS',
                                        'ELETRÔNICOS',
                                        'PRESENTES',
                                        'UTILIDADES DOMÉSTICAS',
                                        'OUTROS'])

                    usuario = menu.opcoes.input_usuario('>>> ')

                    # BLOCO -VARIÁVEIS-MANUTENÇÃO/REPAROS-

                    if usuario is 1:

                        arquivo_manutencao_reparos = 'arquivo_manutencao_reparos'

                        if menu.arquivo.find_file(arquivo_manutencao_reparos) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_manutencao_reparos)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'MANUTENÇÃO/REPAROS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -VARIÁVEIS-ELETRÔNICOS-

                    if usuario is 2:

                        arquivo_educacao_outros = 'arquivo_educacao_outros'

                        if menu.arquivo.find_file(arquivo_educacao_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_educacao_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -VARIÁVEIS-PRESENTES-

                    if usuario is 3:

                        arquivo_presentes = 'arquivo_presentes'

                        if menu.arquivo.find_file(arquivo_presentes) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_presentes)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'PRESENTES'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -VARIÁVEIS-UTILIDADES DOMÉSTICAS

                    if usuario is 4:

                        arquivo_utilidades = 'arquivo_utilidades'

                        if menu.arquivo.find_file(arquivo_utilidades) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_utilidades)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'UTILIDADES DOMÉSTICAS'

                        menu.titulo(titulo, len(titulo))

                    # BLOCO -VARIÁVEIS-OUTROS-

                    if usuario is 5:

                        arquivo_variaveis_outros = 'arquivo_variaveis_outros'

                        if menu.arquivo.find_file(arquivo_variaveis_outros) is False:
                            print(f'{"Arquivo não existente.":^60}'
                                  f'\n{"Criar arquivo?":^60}'
                                  f'\n{"S - SIM / N - NÃO":^60}')

                            usuario = menu.opcoes.input_comum(f'{">>> ":>30}').upper()

                            if usuario == 'S':
                                menu.arquivo.new_file(arquivo_variaveis_outros)
                            else:
                                print('Necessário a criação do arquivo para continuar')
                                break

                        titulo = 'OUTROS'

                        menu.titulo(titulo, len(titulo))

    if usuario == 0:
        break
