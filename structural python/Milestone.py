from collections import Counter
def displayBoard(board):
    """
    i can either use the .format or i use concatenation
    """
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])
#    return f"Player One: {player2} Player Two: {player2}"
myList = ['#','X','O','X','O','X','O','X','O','X']
displayBoard(myList)

def playerInput():
    marker=''
    player1= ''
    while marker != "X" and marker != "O":
        marker= str(input('Player one X or O: '))
    player1=marker
    if player1=='X':
        player2='O'
        print(player2)
    else:
        player2='X'
    return(player1,player2)
print(playerInput())

newList = [x for x in ""*10]
marker = ''
while marker != "X" and marker != "O":
    marker= str(input('Player one X or O: '))
def placeMarker(board,marker,position):
    board[position]=marker
    board = board[position]
    """board[1]=marker
    board[2]=marker
    board[3]=marker
    board[4]=marker
    board[5]=marker
    board[6]=marker
    board[7]=marker
    board[8]=marker
    board[9]=marker"""
    print(board)
placeMarker(myList,marker,3)
displayBoard(myList)

def winCheck(board,mark):
    t = Counter(board)
    fish1=mark
    fish2=""
    if fish1=='X':
        fish2='O'
    else:
        fish2='X'
    if t[fish1] > t[fish2]:
        return(f"{fish1} wins!\n{fish2} loses")
print(winCheck(myList,"O"))