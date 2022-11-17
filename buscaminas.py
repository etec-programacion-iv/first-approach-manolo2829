class Buscaminas:

    def __init__(self, boardX, boardY, bombs):
        self.boardX = boardX
        self.boardY = boardY
        self.bombs = bombs
        self.board = []
        self.show = []
        self.passed = True

    def win(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]== 'B' and self.show[y][x] != 'F':
                    self.passed = False 
        return self.passed

    def lose(self):
        return not self.win()

    def question(self, movs):
        mov = input()
        if not mov in movs:
            raise ValueError("Error")
        row = int(input())
        col = int(input())
        return mov, row, col

    def play(self, mov, row, col):
        if mov == 'uncover':
            self.show[row][col] = self.board[row][col]
        elif mov == 'flag':
            self.show[row][col] = 'F'
        
