class BoardGame:
    def __init__(self, Pname: str = '', LastPlayer: str = '', mark: str ='x', mark2: str ='o', Wins: int = 0, Loses: int = 0, NTies: int = 0, GPlayed: int = 0) -> None:

        '''
            Args:
                Pname: The user name of either player 1 or 2
                LastPlayer: The name of player 1 or 2 after they have had their turn
                NWins: the number of times the game was won by player 1 or 2
                Nloses: the number of times either player 1 or 2 has lost '''
        self.board = [ ['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-'] ] #board[2][1] [2]: row access and [1]: inside the row
        self.Pname = Pname
        self.LastPlayer = LastPlayer
        self.mark = mark
        self.mark2 = mark2
        self.Wins = 0
        self.Loses = 0
        self.Tie = 0
        self.GPlayed = 0
        
    '''' a = [[1, 2, 3],
     [7, 8, 9]]
print(a[1])
[7, 8, 9]
print(a[1][0])
7

print(a[0][2])
3
this is how the player would access a row and put in their input 
'''
    
    def updateGamesPlayed(self, Pname: str ) -> str:
        ''' when player 1 asks the user for the host info of player 2 and recieves
        it the count of this function will increment by 1 or everytime bot player names have been
        given the count increments by 1 (Keeps track of how many games have been played)'''


    def resetGameBoard(self,) -> str:
        ''' each time players win, lose, or tie the game will restart.
        the game will also restart if the borad is full(a tie). (Clears all the moves from game board)'''
        self.board = [ ['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-'] ]
        return self.board
        

    def updateGameBoard(self, row:int = 0, column:int = 0, mark: str = '', mark2: str = '') -> str:
        ''' Each time a player makes a move the game board will update to have that players
        move displayed on the board using the coordinates of each players input (pass as args the row and column of the matrix being created
        and trigger isWinner first then boardIsFull each time a player makes a more(when the board is updated))'''
        for r, c in enumerate(self.board):
            r = row
            c = column
            if mark != '':
                self.board[r][c] = mark
            elif mark != '':
                self.board[r][c] = mark2
    def isWinner(self) -> bool:
        ''' this function will check if the LAST move by either player results in a win
        it will also update the win count of the winning player as well as the loss count of
        the losing player (check if all the win conditions have been met then uses self.NWins and self.NLose to update their count)'''
# MARK wins: horizontal wins ----------------------------------------------------------------
        if (self.board[0][0] == self.mark and self.board[0][1] == self.mark and self.board[0][2] == self.mark) or (self.board[1][0] == self.mark and self.board[1][1] == self.mark and self.board[1][2] == self.mark) or (self.board[2][0] == self.mark and self.board[2][1] == self.mark and self.board[2][2] == self.mark):
            w = True
        else:
            w = False
        if w:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player2':
                self.Loses += 1
            return True
        #vertical wins
        if (self.board[0][0] == self.mark and self.board[1][0] == self.mark and self.board[2][0] == self.mark) or (self.board[0][1] == self.mark and self.board[1][1] == self.mark and self.board[2][1] == self.mark) or (self.board[0][2] == self.mark and self.board[1][2] == self.mark and self.board[2][2] == self.mark):
            w = True
        else:
            w = False
        if w == True:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player2':
                self.Loses += 1
            return True
        #cross wins
        if (self.board[0][0] == self.mark and self.board[1][1] == self.mark and self.board[2][2] == self.mark) or (self.board[0][2] == self.mark and self.board[1][1] == self.mark and self.board[2][0] == self.mark):
            w = True
        else:
            w = False
        if w == True:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player2':
                self.Loses += 1
            return True
#MARK2 wins: horizontal wins ----------------------------------------------------------------
        if (self.board[0][0] == self.mark2 and self.board[0][1] == self.mark2 and self.board[0][2] == self.mark2) or (self.board[1][0] == self.mark2 and self.board[1][1] == self.mark2 and self.board[1][2] == self.mark2) or (self.board[2][0] == self.mark2 and self.board[2][1] == self.mark2 and self.board[2][2] == self.mark2):
            w = True
        else:
            w = False
        if w == True:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player1':
                self.Loses += 1
            return True
        #vertical wins
        if (self.board[0][0] == self.mark2 and self.board[1][0] == self.mark2 and self.board[2][0] == self.mark2) or (self.board[0][1] == self.mark2 and self.board[1][1] == self.mark2 and self.board[2][1] == self.mark2) or (self.board[0][2] == self.mark2 and self.board[1][2] == self.mark2 and self.board[2][2] == self.mark2):
            w = True
        else:
            w = False
        if w == True:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player1':
                self.Loses += 1
            return True
        #cross wins
        if (self.board[0][0] == self.mark2 and self.board[1][1] == self.mark2 and self.board[2][2] == self.mark2) or (self.board[0][2] == self.mark2 and self.board[1][1] == self.mark2 and self.board[2][0] == self.mark2):
            w = True
        else:
            w = False
        if w == True:
            self.Wins += 1
            self.GPlayed += 1
            F = False
            if F == False and self.Pname == 'Player1':
                self.Loses += 1
            return True
    def boardIsFull(self,) -> str:
        ''' checks if no more moves can be mae by either player(a tie) and updates the tie count
        (check if the win condtions have been met or if the no more moves can be made on the matrix and trigger) '''
        if (w[0][0] and w[0][1] and w[0][2]) and (w[1][0] and w[1][1] and w[1][2]) and (w[2][0] and w[2][1] and w[2][2]) == '-': #this is techincally an emppty spot so fix this and chage it from W to self.board
            return True
        if (w[0][0] and w[0][1] and w[0][2]) and (w[1][0] and w[1][1] and w[1][2]) and (w[2][0] and w[2][1] and w[2][2]) == 'x':
            return True
        if (w[0][0] and w[0][1] and w[0][2]) and (w[1][0] and w[1][1] and w[1][2]) and (w[2][0] and w[2][1] and w[2][2]) == 'o':
            return True
    def printStats(self,):
        ''' will print the players name, the name of the last player to make a move, the number of games
        played, number of wins, loses, and ties '''
        stat = (f'Name:{self.Pname},Games Played:{self.GPlayed},Wins:{self.Wins}, Lose:{self.Loses}')
        return stat