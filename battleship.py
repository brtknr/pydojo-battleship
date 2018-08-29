'''
BATTLESHIP
n * m
'''
import random

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
        n_cells = n*m
        for i in range(n):
            column = []
            for j in range(m):
                column.append(Cell())
            board.append(column)
        list_of_ships = list()
        for ship_type in ships:
            for ship in range(int(n_cells*ship_type['percent'])):
                list_of_ships.append(ship_type['length'])
        random.shuffle(list_of_ships)
        for length in list_of_ships:
            while True:
                i,j = random.choice(range(n)), random.choice(range(m))
                orient = random.choice(range(2))
                free = True
                # Brute force and determine if the slot of that length is free
                for k in range(length):
                    if orient == 0:
                        if board[(i+k)%n][j].has_ship:
                            free = False
                    if orient == 1:
                        if board[i][(j+k)%m].has_ship:
                            free = False
                # Populate those cells with a ship and break loop
                if free == True:
                    for k in range(length):
                        if orient == 0:
                            board[(i+k)%n][j].has_ship = True
                        if orient == 1:
                            board[i][(j+k)%m].has_ship = True
                    break
            print (length)

                        
        self.board = board

    def __repr__(self):
        return '\n'.join([''.join([str(col) for col in row]) for row in self.board])

    def to_json(self):
        b = []
        for row in self.board:
            column = []
            for c in row:
                v = 0 # nothjing
                if c.hit:
                    if c.has_ship:
                        v = 2 # hit a ship
                    else:
                        v = 1 # missed
                column.append(v)
            b.append(column)
        return b

game = Game(n, m, ships)
#game.board[1][1].hit = True

'''
for i in range(30):
    x, y = random.randint(0, n-1), random.randint(0, m-1)
    game.board[x][y].hit = True
'''

print(game)
