#primer juego. Ta te ti - tic tac toe

#import itertools for the games combination
import itertools
from IPython.display import clear_output

movimientos = []
players = {}
winner_combinations = (('1','2','3'), ('4','5','6'), ('7','8','9'), ('1','4','7'), ('2','5','8'), ('3','6','9'), ('1','5','9'), ('3','5','7'))

def knowplayer(pla):
    if pla==1:
        return players['player1']
    else:
        return players['player2']


def dibujarTablero(movs=[]):
    clear_output()
    po1,po2,po3,po4,po5,po6,po7,po8,po9=' ',' ',' ',' ',' ',' ',' ',' ',' '
    for x in range(0,len(movs)):
        locals()["po"+str(movs[x][1])] = knowplayer(movs[x][0])

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



def verif_mov(x):
    #verify that the mov doesnt exist
    if 10 > x > 0 :
        movs_made = [x[1] for x in movimientos]
        return x in movs_made
    else:
        print('Errror. You must set a value between 1-9')

def setplayers():
    players['player1']=input('Player 1, choose your side: X - O \n').upper()
    if players['player1']=='X':
        players['player2']='O'
    else:
        players['player2']='X'

    print('Player 1 = ' + players['player1'])
    print('player 2 = ' + players['player2'])


def verif_winner(player):
    mov_player1 = [str(x[1]) for x in movimientos if x[0]==player]
    mov_player1.sort()
    mov_player1 = tuple(mov_player1)

    combinaciones_tot = itertools.permutations(mov_player1)
    for x in combinaciones_tot:
        return x in winner_combinations

#________________________________________________________________
#________________________________________________________________
#________________________________________________________________


setplayers()
dibujarTablero()

player=1
newgame = 'Yes'
while newgame == 'Yes':
    newgame=''
    for x in range(1,9):
        mov_made = int(input(f'Make your move Player {player} = '))
        if verif_mov(mov_made) == False:
            movimientos.append((player, mov_made))
            dibujarTablero(movimientos)
        
        if x>4 :
            if verif_winner(player) == True:
                print('CONGRATS player '+ str(player) +' is the winner!!!! ')
                break

        if player==1:
            player=2
        elif player==2:
            player=1
    
    newgame = input('would you like to play a new game? Yes or No')