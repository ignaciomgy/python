#primer juego. Ta te ti - tic tac toe
po1,po2,po3,po4,po5,po6,po7,po8,po9=' ',' ',' ',' ',' ',' ',' ',' ',' '

movimientos = []

def konwplayer(pla):
    if pla==1:
        return player1
    else:
        return player2


def dibujarTablero(movs=[]):
    for x in range(0,len(movs)):

        globals()["po"+str(movs[x][1])] = konwplayer(movs[x][0])


    print('   |   |   ')
    print(f' {po1} | {po2} | {po3} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {po4} | {po5} | {po6} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {po7} | {po8} | {po9} ')
    print('   |   |   ')
    
player1 = input('Player 1, choose your side: X - O \n').upper()
if player1=='X':
    player2='O'
else:
    player2='X'

print('Player 1 = ' + player1)
print('player 2 = ' + player2)
dibujarTablero()


player=1
for x in range(1,9):
    movimientos.append((player, verif_mov(int(input(f'Make your move Player {player} = ')))))
    dibujarTablero(movimientos)



    if player==1:
        player=2
    elif player==2:
        player=1

    






