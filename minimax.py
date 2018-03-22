

class MiniMax:
    def __init__(self, board):
        self.board = [x[:] for x in board]


    def gameOver(self, state):
        if self.findStreak(state, 1, 4) >= 1:
            return True
        elif self.findStreak(state, 2, 4) >= 1:
            return True
        else:
            return False

    def isValidMove(self, col, state):
        for i in range(6):
            if not state[i][col]:
                return True;

        return False;

    def makeMove(self, state, col, currPlayer):

        temp = [x[:] for x in state]
        for i in range(5, -1, -1):
            if not temp[i][col]:
                temp[i][col] = currPlayer
                return temp


    def bestMove(self, depth, state, currPlayer):

        #if self.gameOver(state):
        #    return None 

        if currPlayer == 1:
            oppPlayer = 2
        else:
            oppPlayer = 1

        legalMoves = {}
        for col in range(7):
            if self.isValidMove(col, state):
                tempMove = self.makeMove(state, col, currPlayer)
                legalMoves[col] = self.searchStateSpace(depth - 1, tempMove,
                                                        oppPlayer)

        moves = legalMoves.items()
        answ = []
        for move, alpha in moves:
            answ.append(alpha)

        return answ.index(min(answ))


    def maxMove(self, depth, state, currPlayer, alpha, beta):
        legalMoves = []

        for i in range(7):
            if self.isValidMove(i, state):
                temp = self.makeMove(state, i, currPlayer)
                legalMoves.append(temp)

        if depth == 0 or len(legalMoves) == 0 or self.gameOver(state):
            return self.eval(state, currPlayer, depth)


        if currPlayer == 1:
            oppPlayer = 2
        else:
            oppPlayer = 1

        for child in legalMoves:
            move = minMove(depth -1 , child, oppPlayer, alpha, beta)
            if self.eval(move) > self.eval(best_move):
                best_move = move
                alpha = self.eval(move)
            if (beta > alpha):
                return best_move

        return best_move


    def searchStateSpace(self, depth, state, currPlayer):
        legalMoves = []

        for i in range(7):
            if self.isValidMove(i, state):
                temp = self.makeMove(state, i, currPlayer)
                legalMoves.append(temp)

        if depth == 0 or len(legalMoves) == 0 or self.gameOver(state):
            return self.eval(state, currPlayer, depth)


        if currPlayer == 1:
            oppPlayer = 2
        else:
            oppPlayer = 1

        alpha = float('-inf')
        for child in legalMoves:
            if child == None:
                print "child == None (search)"
            alpha = max(alpha, -self.searchStateSpace(depth-1, child, oppPlayer))
        return alpha




    def eval(self, state, currPlayer, depth):

        if currPlayer == 1:
            oppPlayer = 2
        else:
            oppPlayer = 1

        numFours = self.findStreak(state, currPlayer, 4)
        numThrees = self.findStreak(state, currPlayer, 3)
        numTwos = self.findStreak(state, currPlayer, 2)

        humFours = self.findStreak(state, oppPlayer, 4)
        humThrees= self.findStreak(state, oppPlayer, 3)
        humTwos= self.findStreak(state, oppPlayer, 2)

        if humFours > 0:
            return -100000 - depth

        return (numFours * 100000 + numThrees * 100 + numTwos) - (humThrees*100
                                                        + humTwos) + depth

    def findStreak(self, state, currPlayer, streak):
        count = 0
        # for each piece in the board...
        for i in range(6):
            for j in range(7):
            # ...that is of the color we're looking for...
                if state[i][j] == currPlayer:
                    # check if a vertical streak starts at (i, j)
                    count += self.verticalStreak(i, j, state, streak)

                    # check if a horizontal four-in-a-row starts at (i, j)
                    count += self.horizontalStreak(i, j, state, streak)

                    # check if a diagonal (either way) four-in-a-row starts at (i, j)
                    count += self.diagonalCheck(i, j, state, streak)
        # return the sum of streaks of length 'streak'
        return count






    def verticalStreak(self, row, col, state, streak):
        consecutiveCount = 0
        for i in range(row, 6):
            if state[i][col] == state[row][col]:
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def horizontalStreak(self, row, col, state, streak):
        consecutiveCount = 0
        for j in range(col, 7):
            if state[row][j] == state[row][col]:
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def diagonalCheck(self, row, col, state, streak):

        total = 0
        # check for diagonals with positive slope
        consecutiveCount = 0
        j = col
        for i in range(row, 6):
            if j > 6:
                break
            elif state[i][j] == state[row][col]:
                consecutiveCount += 1
            else:
                break
            j += 1 # increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        # check for diagonals with negative slope
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j] == state[row][col]:
                consecutiveCount += 1
            else:
                break
            j += 1 # increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        return total









