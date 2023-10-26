#Marguerite Sutedjo and Richard He
#I pledge my honor that I have abided by the Stevens Honor System.

class Board():
    def __init__(self, width = 7, height = 6):
        '''constructor'''
        self.__width = width
        self.__height = height
        board = []
        row = []
        for w in range(width):
            row.append(' ')
        for h in range(height):
            board.append(list(row))
        
        self.__boardArray = board

    def __str__(self):
        '''returns string representation of board'''
        x = ''
        for h in range(self.__height):
            for w in range(self.__width):
                x += '|' + str(self.__boardArray[h][w])
            x += '| \n'
        x += '-' * 15 + '\n' + ' 0 1 2 3 4 5 6 '
        return x

    def hostGame(self):
        '''runs a loop allowing the user to play the game'''
        print('Welcome to Connect 4!')
        
        x = True
        checker = ''
        while not self.winsFor(checker):
            print(self.__str__())
            prompt = ''
            if x:
                prompt = "X's Choice: "
                checker = 'X'
            else:
                prompt = "O's Choice: "
                checker = 'O'
            moveComplete = False
            while not moveComplete:
                c = input(prompt)
                validInput = False
                try:
                    test = int(c)
                    if test >= 0 and test <= 6:
                        c = test
                        validInput = True
                except ValueError:
                    print('Please enter a number.' )
                if validInput:
                    if self.allowsMove(c):
                        self.addMove(c, checker)
                        moveComplete = True
                    else:
                        print('No more room. Try again')
                else:
                    print('Not a valid column.')
            x = not x
        

    def allowsMove(self, col):
        '''returns True if calling Board can allow a move into column c, returns False if c does not have space available'''
        for h in range(self.__height):
            if self.__boardArray[h][col] == ' ':
                return True
        return False

    def addMove(self, col, ox):
        '''add ox checker'''
        for h in range(self.__height - 1, -1, -1):
            if self.__boardArray[h][col] == ' ':
                self.__boardArray[h][col] = ox
                break
        
    def setBoard(self, moveString): 
        """ takes in a string of columns and places 
            alternating checkers in those columns, 
            starting with 'X' 
             
            For example, call b.setBoard('012345') 
            to see 'X's and 'O's alternate on the 
            bottom row, or b.setBoard('000000') to 
            see them alternate in the left column. 
 
            moveString must be a string of integers 
        """ 
        nextCh = 'X'   # start by playing 'X' 
        for colString in moveString: 
            col = int(colString) 
            if 0 <= col <= self.__width: 
                self.addMove(col, nextCh) 
            if nextCh == 'X': nextCh = 'O' 
            else: nextCh = 'X'
    
    def winsFor(self, ox):
        '''returns True if given checker, 'X' or 'O', held in ox, has won the calling Board. It should return False otherwise'''
        result = (False, ' ')
        currChecker = ' '
        spaces = 0
        for c in range(self.__width):
            for r in range(self.__height):
                if self.__boardArray[r][c] == ' ':
                    spaces += 1
                    
        # check left and right
        for r in range(self.__height):
            for c in range(self.__width - 3):
                currChecker = self.__boardArray[r][c]
                #print([r,c],currChecker)
                if self.__boardArray[r][c] != ' ' and self.__boardArray[r][c] == currChecker and self.__boardArray[r][c+1] == currChecker and self.__boardArray[r][c+2] == currChecker and self.__boardArray[r][c+3] == currChecker:
                    result = (True, currChecker)

        #check up and down
        for c in range(self.__width):
            for r in range(self.__height - 3):
                currChecker = self.__boardArray[r][c]
                #print([r,c],currChecker)
                if self.__boardArray[r][c] != ' ' and self.__boardArray[r][c] == currChecker and self.__boardArray[r+1][c] == currChecker and self.__boardArray[r+2][c] == currChecker and self.__boardArray[r+3][c] == currChecker:
                    result = (True, currChecker)

        #check / diagonal spaces
        for c in range(self.__width - 3):
            for r in range(3, self.__height):
                currChecker = self.__boardArray[r][c]
                #print([r,c],currChecker)
                if self.__boardArray[r][c] != ' ' and self.__boardArray[r][c] == currChecker and self.__boardArray[r-1][c+1] == currChecker and self.__boardArray[r-2][c+2] == currChecker and self.__boardArray[r-3][c+3] == currChecker:
                    result = (True, currChecker)

        #check \ diagonal spaces
        for c in range(self.__width - 3):
            for r in range(self.__height - 3):
                currChecker = self.__boardArray[r][c]
                #print([r,c],currChecker)
                if self.__boardArray[r][c] != ' ' and self.__boardArray[r][c] == currChecker and self.__boardArray[r+1][c+1] == currChecker and self.__boardArray[r+2][c+2] == currChecker and self.__boardArray[r+3][c+3] == currChecker:
                    result = (True, currChecker)
        win = ""
        
        if result[0]:
            if result[1] == 'X':
                win = "X Wins!"
            elif result[1] == 'O':
                win = "O Wins!"
    
        
        if result[0] and result[1] == ox:
            print(self.__str__())
            print(win)
            return True
        elif spaces == 0:
            print(self.__str__())
            print("Board is Full")
            return True
        
        return False



    
        

        
    
