
def display_Board(a):
    print(a[9]+"| "+ a[8]+"| "+ a[7]+"|\n")
    print(a[6]+"| " +a[5]+"| "+ a[4]+"|\n")
    print(a[3]+"| " +a[2]+"| " +a[1]+"|")

#a=['#','X','O','X','O','X','O','X','O','X']
#display_Board(a)

def player_input():
    player2=''
    marker=input("Player one Which do you want to play with X or O: ")
    player1=marker.upper()
    while player1!='X' and player1!='O':
        marker=input("Invalid input try again: ")
        player1=marker.upper()
    if player1=='X':
        player2='O'
    else:
        player2='X'
    t=[player1,player2]
    return t
t=player_input()
player1=t[0]
player2=t[1]
print(player_input())

def place_marker(a,marker):
    #a=[marker for x in range(1,10)]
    while True:
        position=int(input("Player1, input a number between 1 and 9: "))
        pos=position
        a[pos]=player1
        print("\n"*100)
        display_Board(a)
        if a[4]==player1 and a[5]==player1 and a[6]==player1:
            print("player1 won!")
            break
        position=int(input("Player2, input a number between 1 and 9: "))
        pos=position
        a[pos]=player2
        print("\n"*100)
        display_Board(a)
        if a[4]==player2 and a[5]==player2 and a[6]==player2:
            print("player2 won!")
            break
test_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
place_marker(test_board,player1)