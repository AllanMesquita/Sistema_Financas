tabuleiro = {1:'1',
      2:'2',
      3:'3',
      4:'4',
      5:'5',
      6:'6',
      7:'7',
      8:'8',
      9:'9'}

jaEscolhido = [5]
player = 0
pc = 0


def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print(f'+-------+-------+-------+'
          f'\n|       |       |       |'
          f'\n|   {board[1]}   |   {board[2]}   |   {board[3]}   |'
          f'\n|       |       |       |'
          f'\n+-------+-------+-------+'
          f'\n|       |       |       |'
          f'\n|   {board[4]}   |   {board[5]}   |   {board[6]}   |'
          f'\n|       |       |       |'
          f'\n+-------+-------+-------+'
          f'\n|       |       |       |'
          f'\n|   {board[7]}   |   {board[8]}   |   {board[9]}   |'
          f'\n|       |       |       |'
          f'\n+-------+-------+-------+')


def EnterMove():

# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision
#
    global player, tabuleiro

    while True:
        player = int(input('Onde deseja fazer a sua jogada? '
                           '\n>>> '))
        if MakeListOfFreeFields(player) is False:
            continue
        else:
            break

    tabuleiro[player] = 'O'


def MakeListOfFreeFields(jogador):
#
# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    global jaEscolhido

    if jogador in jaEscolhido:
        return False
    else:
        jaEscolhido.append(jogador)
        return True


def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if
# the player using 'O's or 'X's has won the game
#
    if tabuleiro[1] is sign and tabuleiro[2] is sign and tabuleiro[3] is sign:
        return True
    elif tabuleiro[4] is sign and tabuleiro[5] is sign and tabuleiro[6] is sign:
        return True
    elif tabuleiro[7] is sign and tabuleiro[8] is sign and tabuleiro[9] is sign:
        return True
    elif tabuleiro[1] is sign and tabuleiro[4] is sign and tabuleiro[7] is sign:
        return True
    elif tabuleiro[2] is sign and tabuleiro[5] is sign and tabuleiro[8] is sign:
        return True
    elif tabuleiro[3] is sign and tabuleiro[6] is sign and tabuleiro[9] is sign:
        return True
    elif tabuleiro[1] is sign and tabuleiro[5] is sign and tabuleiro[9] is sign:
        return True
    elif tabuleiro[3] is sign and tabuleiro[5] is sign and tabuleiro[7] is sign:
        return True
    else:
        return False


def DrawMove():
#
# the function draws the computer's move and updates the board
#
    global pc, tabuleiro

    from random import randint

    while True:
        pc = randint(1, 9)

        if MakeListOfFreeFields(pc) is False:
            continue
        else:
            break

    tabuleiro[pc] = 'X'


print('Olá, vamos jogar!'
      '\nEu sempre começo.'
      '\nEu escolho a posição 5.')

tabuleiro[5] = 'X'

DisplayBoard(tabuleiro)

for jogada in range(8):
    EnterMove()
    DisplayBoard(tabuleiro)
    if VictoryFor(tabuleiro, 'O') is True:
        print('Você ganhou.')
        break
    DrawMove()
    DisplayBoard(tabuleiro)
    if VictoryFor(tabuleiro, 'X') is True:
        print('HAHA! Eu ganhei.')
        break
    if len(jaEscolhido) == 9:
        print('Empate.')
        break
