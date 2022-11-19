import socket
from GameBoard import BoardGame



def GetConnected():
    '''client(receives) server this is player2'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 5678))
    SC = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '\ |', ']', '[', '}', '{', '.', '/',
          '<', '>', '?', '~']
    server_uname = s.recv(1024)
    print("Server player name: ", server_uname.decode())
    client_uname = None
    while client_uname == None:
        client_uname = input("Please send player1 your username:\n")
        count = 0
        for i in client_uname:
            if i in SC:
                count +=1
        if count > 0:
            client_uname = None
        elif count == 0:
            s.sendall(client_uname.encode())
    connected = True
    return s
 
def winner():
    while True:
        player1 = BoardGame('Player1', 'Player1', 'x', 0, 0, 0)
        if player1.isWinner() is True:
            ask = input('You win! Would you like to play again?:(y or n)\n')
            if ask == 'y' or 'Y':
                print('Play Again')
            elif ask == 'n' or 'N':
                print('Fun Times')
                break
def PlayAgain(s):
    PlayGame(s)

def PlayGame(s):
    player2 = BoardGame('Player2', 'Player2','x','o', 0, 0,0)
    connected = True
    winCount = 0
    while connected:
# this section of the code recieves the other players move and updates player2's board:
        Host_msg1 = s.recv(1024)
        Host_msg2 = s.recv(1024)
        print(Host_msg1.decode())
        print(Host_msg2.decode())
        player2.updateGameBoard(int(Host_msg1), int(Host_msg2), 'x')
        if winCount >= 0:
            x = player2.isWinner()
            if winCount >= 2:
                if x == False:
                    PlayAgain(s)

# this section of the code sends player2's moves to the other player:
        winCount += 1
        print(player2.board)
        if player2.Loses >= 1:
            PMsg = s.recv(1024).decode()
            if PMsg == 'Play Again':
                print(PMsg)
                #PlayAgain(s)
            EMsg = s.recv(1024).decode()
            if EMsg == 'Fun Times':
                print(player2.printStats())
                player2.resetGameBoard()
                s.close()
                quit()

        client1_msg = input('Pick a row(0-2):\n')
        if (client1_msg == '0') or (client1_msg == '1') or (client1_msg == '2'):
            s.sendall(client1_msg.encode())
        else:
            continue
        client2_msg = input('Pick a column(0-2):\n')
        if (client2_msg == '0') or (client2_msg == '1') or (client2_msg == '2'):
            s.sendall(client2_msg.encode())
        else:
            continue
        player2.updateGameBoard(int(client1_msg), int(client2_msg), player2.mark2)
    s.close()


if __name__ == '__main__':
    s = GetConnected()
    PlayGame(s)
    PlayAgain(s)