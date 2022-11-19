import socket
from GameBoard import BoardGame

'''this server sends information this is player1'''


#Host = 'localhost' # Standard loopback interface address (localhost)
#Port = 5670  # Port to listen on (non-privileged ports are > 1023)


def run_server():
    Port = int(input('Please provide your password information:\n'))
    Host = str(input('Please provide your username information:\n'))
    Hsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Hsocket.bind((Host, Port))
    Hsocket.listen(1)

    username = 'Player1'
    conn, addr = Hsocket.accept()
    print("Connected : ", addr)
    conn.sendall(username.encode())
    client_uname = conn.recv(1024)
    client = client_uname.decode()
    print(client)
    return conn #have to return the connection not the socket bc the host server can talk(connect) to multiple clients at once

def PlayAgainR(h):
    go = 'Play Again'
    stop = 'Fun Times'
    gplayed = 0
    ask = input('Would you like to play again?(y or n):\n')
    player1 = BoardGame('Player1', 'Player1', 'x','o', 0, 0, 0,0)
    if ask == 'y' or ask == 'Y':
        #player1.GPlayed += 1
        h.sendall(str(go).encode())
        player1.resetGameBoard()
        PlayGame(h)
    if ask == 'n' or ask == 'N':
        h.sendall(str(stop).encode())
        h.close()
        quit()
def PlayGame(h):
    player1 = BoardGame('Player1', 'Player1','x','o', 0, 0,0)
    connected = True
    winCount = 0
    while connected:
# this section of the code sends player1's moves to the other player:
        winCount += 1
        print(player1.board)#this is where I print the board
        client1_msg = input('Pick a row(0-2):\n')
        if (client1_msg == '0') or (client1_msg == '1') or (client1_msg == '2'):
            h.sendall(client1_msg.encode())
        else:
            continue
        client2_msg = input('Pick a column(0-2):\n')
        if (client2_msg == '0') or (client2_msg == '1') or (client2_msg == '2'):
            h.sendall(client2_msg.encode())
        else:
            continue
        player1.updateGameBoard(int(client1_msg), int(client2_msg), player1.mark)
        x = player1.isWinner()
        if x == True:
            print(player1.printStats())
            PlayAgainR(h)


# this section of the code receives the other players move and updates player1's board:
        Host_msg1 = h.recv(1024)
        Host_msg2 = h.recv(1024)
        print(Host_msg1.decode())
        print(Host_msg2.decode())
        try:
            player1.updateGameBoard(int(Host_msg1), int(Host_msg2), 'o')
        except:
            pass
    h.close()
if __name__ == "__main__":
   h = run_server()
   PlayGame(h)
   PlayAgainR(h)