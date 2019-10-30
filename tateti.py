class TaTeTi():

    def __init__(self, table = None):
        if not table:
            self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        else:
            self.board = table

    def full(self):
        if self.board.count(' ') > 0:
            return False
        else:
            return True

    def win(self):
        rows = [[self.board[0],self.board[1], self.board[2]], [self.board[3], self.board[4], self.board[5]], [self.board[6], self.board[7], self.board[8]]]

        columns = [[self.board[0],self.board[3], self.board[6]], [self.board[1], self.board[4], self.board[7]], [self.board[2], self.board[5], self.board[8]]]

        diagonals = [[self.board[0], self.board[4], self.board[8]], [self.board[2], self.board[4], self.board[6]]]

        lines = rows + columns + diagonals
        
        for line in lines:
            if (all(board_position == 'x' for board_position in line) or all(board_position == 'o' for board_position in line)):
               return True

    def validate(self, position):
        return self.board[position-1] == " "

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position-1] = piece
        else:
            raise Exception

    def draw_board(self):
        self.display = "\n"
        for number in range(9):
            if self.board[number] != " ":
                self.display += " " + self.board[number] + " "
            else:
                self.display += " " + str(1+number) + " "
            if number == 2 or number == 5:
                self.display += "\n---+---+---\n"
            elif number == 8:
                self.display += "\n"
            else:
                self.display += "|"

        return self.display