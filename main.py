'''
BATTLESHIP
n * m
'''

n = 10
m = 10

ships = [
            dict(name="boat", length=1, percent=0.1),
            dict(name="ship",length=2, percent=0.1),
            dict(name="sub",length=3, percent=0.1),
        ]

class Cell(object):
    def __init__(self):
        # 0 = empty
        self.hit = False
        self.has_ship = False

    def __repr__(self):
        if self.hit:
            if self.has_ship:
                return '[X]'
            else:
                return '[O]'
        else:
            return '[ ]'

class Game(object):
    def __init__(self, n, m, ships):
        board = []
        for i in range(n):
            column = []
            for j in range(m):
                column.append(Cell())
            board.append(column)
        self.board = board

    def __repr__(self):
        r = ''
        for row in self.board:
            for c in row:
                r += str(c)
            r += '\n'
        return r[:-1]


game = Game(n, m, ships)
game.board[1][1].hit = True
print(game)
