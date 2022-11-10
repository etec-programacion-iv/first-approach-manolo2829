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
            row = self.board[y]
            position_y = y
            for position_x in range(len(row)):
                board_position= self.board[position_y][position_x]
                show_position = self.show[position_y][position_x]
                if(board_position== 'B'):
                    if(show_position == 'F'):
                        pass;
                    else:
                        aprove = False

        return aprove

    def lose(self):
        if self.win():
            return False
        else: 
            return True


# buscaminas = Buscaminas(8, 8, 10)
# buscaminas.board =  [['2', 'B', '2', ' ', '1', 'B', 'B', '1'],
#                     ['3', 'B', '3', ' ', '1', '3', '3', '2'],
#                     ['3', 'B', '3', ' ', ' ', '1', 'B', '1'],
#                     ['4', 'B', '3', ' ', ' ', '1', '1', '1'],
#                     ['B', 'B', '2', ' ', ' ', ' ', ' ', ' '],
#                     ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
#                     [' ', ' ', '1', 'B', '1', ' ', ' ', ' ']]
# buscaminas.show = [[' ', '1', 'F', 'F', '1', ' ', '1', 'F'],
#                     ['1', '2', '2', '2', '1', ' ', '1', '1'],
#                     ['B', '3', '2', '1', ' ', ' ', '1', '1'],
#                     ['2', 'F', 'F', '2', ' ', ' ', '1', 'F'],
#                     ['2', '4', 'F', '2', ' ', ' ', '1', '1'],
#                     ['1', 'F', '3', '2', ' ', ' ', ' ', ' '],
#                     ['1', '2', 'F', '1', ' ', ' ', ' ', ' '],
#                     [' ', '1', '1', '1', ' ', ' ', ' ', ' ']]


# print(buscaminas.win())
# print(buscaminas.lose())