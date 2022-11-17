class Buscaminas:

    def __init__(self, boardX, boardY, bombs):
        self.boardX = boardX
        self.boardY = boardY
        self.bombs = bombs
        self.board = []
        self.show = []

    def win(self):
        aprove = True
        for y in range(len(self.board)):
            position_y = y
            for position_x in range(len(self.board[y])):
                board_position= self.board[position_y][position_x]
                show_position = self.show[position_y][position_x]
                if(board_position== 'B' and show_position =='F'):
                    pass
                else:
                    aprove = False 
        return aprove

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
        
