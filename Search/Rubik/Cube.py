from copy import deepcopy


class Cube:
    def __init__(self):
        self.sides = {}
        for color in ['Green', 'Red', 'White', 'Orange', 'Blue', 'Yellow']:
            self.sides[color] = {}
            for n in range(1,10):
                self.sides[color][n] = (color[:1], n)
        self.goal_state = deepcopy(self.sides)

    def __str__(self):
        sp = '       '
        string = ''
        for side in self.sides:
            if side == 'Green' or side == 'Blue' or side == 'Yellow':
                for i in range(3):
                    string += sp + '|' + self.sides[side][1+(i*3)][0] + '|' + self.sides[side][2+(i*3)][0] + '|' + self.sides[side][3+(i*3)][0] + '|\n'
            if side == 'Red':
                for i in range(3):
                    for color in ['Red', 'White', 'Orange']:
                        string += '|' + self.sides[color][1 + (i * 3)][0] + '|' + self.sides[color][2 + (i * 3)][0] + '|' + self.sides[color][3 + (i * 3)][0] + '|'
                        if color == 'Orange':
                            string += '\n'
        return string

    def copy(self):
        new_cube = Cube()
        new_cube.sides = deepcopy(self.sides)
        return new_cube

    def rotate_left(self, side):
        '''
        :param side: it must be one of the dictionaries of self.sides
        :action: it rotate the collors of the chosen side
        '''
        new_side = side.copy()
        new_side[1], new_side[2], new_side[3] = side[3], side[6], side[9]
        new_side[4], new_side[5], new_side[6] = side[2], side[5], side[8]
        new_side[7], new_side[8], new_side[9] = side[1], side[4], side[7]
        return new_side

    def rotate_right(self, side):
        '''
        :param side: it must be one of the dictionaries of self.sides
        :action: it rotate the colors of the chosen side
        '''
        new_side = side.copy()
        new_side[1], new_side[2], new_side[3] = side[7], side[4], side[1]
        new_side[4], new_side[5], new_side[6] = side[8], side[5], side[2]
        new_side[7], new_side[8], new_side[9] = side[9], side[6], side[3]
        return new_side

    ############################################################
    # all the methods below represent the Rubik notation move  #
    ############################################################

    def F(self):
        ex_sides = deepcopy(self.sides)
        self.sides['Blue'] = self.rotate_right(self.sides['Blue'])
        for f, seq_f, t, seq_t in (('Red',(7,8,9), 'White',(7,8,9)), ('White',(7,8,9), 'Orange',(7,8,9)), ('Orange',(7,8,9), 'Yellow',(3,2,1)), ('Yellow',(3,2,1), 'Red',(7,8,9))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def R(self):
        ex_sides = deepcopy(self.sides)
        self.sides['Orange'] = self.rotate_right(self.sides['Orange'])
        for f, seq_f, t, seq_t in (('Yellow',(3,6,9), 'Blue',(3,6,9)), ('Blue',(3,6,9), 'White',(3,6,9)), ('White',(3,6,9), 'Green',(3,6,9)), ('Green',(3,6,9), 'Yellow',(3,6,9))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def U(self):
        ex_sides = deepcopy(self.sides)
        self.sides['White'] = self.rotate_right(self.sides['White'])
        for f, seq_f, t, seq_t in (('Blue',(1,2,3), 'Red',(3,6,9)), ('Red',(9,6,3), 'Green',(7,8,9)), ('Green',(7,8,9), 'Orange',(1,4,7)), ('Orange',(1,4,7), 'Blue',(3,2,1))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def L(self):
        ex_sides = deepcopy(self.sides)
        self.sides['Red'] = self.rotate_right(self.sides['Red'])
        for f, seq_f, t, seq_t in (('Yellow', (1, 4, 7), 'Green', (1, 4, 7)), ('Green', (1, 4, 7), 'White', (1, 4, 7)),
                                   ('White', (1, 4, 7), 'Blue', (1, 4, 7)), ('Blue', (1, 4, 7), 'Yellow', (1, 4, 7))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def B(self):
        ex_sides = deepcopy(self.sides)
        self.sides['Green'] = self.rotate_right(self.sides['Green'])
        for f, seq_f, t, seq_t in (('White', (1, 2, 3), 'Red', (1, 2, 3)), ('Red', (3, 2, 1), 'Yellow', (7, 8, 9)),
                                   ('Yellow', (7, 8, 9), 'Orange', (3, 2, 1)), ('Orange', (1, 2, 3), 'White', (1, 2, 3))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def D(self):
        ex_sides = deepcopy(self.sides)
        self.sides['Yellow'] = self.rotate_right(self.sides['Yellow'])
        for f, seq_f, t, seq_t in (('Blue', (7, 8, 9), 'Orange', (9, 6, 3)), ('Orange', (9, 6, 3), 'Green', (3, 2, 1)),
                                   ('Green', (1, 2, 3), 'Red', (7, 4, 1)), ('Red', (1, 4, 7), 'Blue', (7, 8, 9))):
            for i in range(3):
                self.sides[t][seq_t[i]] = ex_sides[f][seq_f[i]]

    def rewind(self, function):
        def func():
            function()
            function()
            function()
        return func

    def moves(self):
        return {'F': self.F, 'R': self.R, 'U': self.U, 'L': self.L, 'B': self.B, 'D': self.D,\
                'Fi': self.rewind(self.F), 'Ri': self.rewind(self.R), 'Ui': self.rewind(self.U),\
                'Li': self.rewind(self.L), 'Bi': self.rewind(self.B), 'Di': self.rewind(self.D)}

    def check_goal(self):
        if self.sides == self.goal_state:
            return True
        else:
            return False




