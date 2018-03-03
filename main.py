print('Welcome to Tic Tac Toe')
print("\n")
def display_board():
    print( board[1] + "  | " + board[2] + " | " + board[3])
    print("-------------")
    print( board[4] + "  | " + board[5] + " | " + board[6])
    print("-------------")
    print( board[7] + "  | " + board[8] + " | " + board[9])

def check():
    if (board[1]=='X' and board[2]=='X' and board[3]=='X') or (board[1]=='O' and board[2]=='O' and board[3]=='O'):
        if board[1]=='X':
          print("\n\nPlayer 1 is the Winner\n\n")
        else:
          print("\n\nPlayer 2 is the Winner\n\n")
        board[1] = 'W'
        board[2] = 'W'
        board[3] = 'W'
        display_board()
        exit()
    elif (board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[1]=='O' and board[5]=='O' and board[9]=='O'):
        if board[1]=='X':
           print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[1] = 'W'
        board[5] = 'W'
        board[9] = 'W'
        display_board()
        exit()
    elif (board[2]=='X' and board[4]=='X' and board[6]=='X') or (board[2]=='O' and board[4]=='O' and board[6]=='O'):
        if board[2]=='X':
           print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[2] = 'W'
        board[4] = 'W'
        board[6] = 'W'
        display_board()
        exit()
    elif (board[0]=='X' and board[3]=='X' and board[6]=='X') or (board[0]=='O' and board[3]=='O' and board[6]=='O'):
        if board[0] == 'X':
            print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[0] = 'W'
        board[3] = 'W'
        board[6] = 'W'
        display_board()
        exit()
    elif (board[2]=='X' and board[5]=='X' and board[8]=='X') or (board[2]=='O' and board[5]=='O' and board[8]=='O'):
        if board[2] == 'X':
            print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[2] = 'W'
        board[5] = 'W'
        board[8] = 'W'
        display_board()
        exit()
    elif (board[3]=='X' and board[4]=='X' and board[5]=='X') or (board[3]=='O' and board[4]=='O' and board[5]=='O'):
        if board[3] == 'X':
            print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[3] = 'W'
        board[4] = 'W'
        board[5] = 'W'
        display_board()
        exit()
    elif (board[6]=='X' and board[7]=='X' and board[8]=='X') or (board[6]=='X' and board[7]=='X' and board[8]=='X'):
        if board[6] == 'X':
            print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[6] = 'W'
        board[7] = 'W'
        board[8] = 'W'
        display_board()
        exit()
    elif (board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[1]=='O' and board[4]=='O' and board[7]=='O'):
        if board[1] == 'X':
            print("\n\nPlayer 1 is the Winner\n\n")
        else:
            print("\n\nPlayer 2 is the Winner\n\n")
        board[1] = 'W'
        board[4] = 'W'
        board[7] = 'W'
        display_board()
        exit()

board=['-','-','-','-','-','-','-','-','-','-']
t=1;
while t<10:
    if t%2!=0:
        x = input("Player 1 turn: Enter X Position[1-9]:")
        if board[int(x)]=='X' or board[int(x)]=='O':
            print("Position already Taken. Try Different Position")
            pass
        else:
           board[int(x)]='X'
           t += 1
           check()
           display_board()
    else:
        x = input("Player 2 turn: Enter O Position[0-8]:")
        if board[int(x)]=='X' or board[int(x)]=='O':
            print("Position already Taken. Try Different Position")
            pass
        else:
            board[int(x)]='O'
            t+=1
            check()
            display_board()

