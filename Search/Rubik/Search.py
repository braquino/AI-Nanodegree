from copy import deepcopy
from Cube import Cube

def searchDFS(cube):

    for depth in range(1, 999):
        moves = []
        explored = []
        print(depth)
        attempt = rec_search(cube, moves, explored, depth)
        if attempt:
            return attempt


def rec_search(cube, moves, explored, depth):
    #print(cube)
    if cube.check_goal():
        return moves
    if cube.sides in explored or depth == 0:
        return False
    legal_moves = cube.moves()
    explored += [deepcopy(cube.sides)]
    for func in legal_moves:
        new_cube = cube.copy()
        new_cube.moves()[func]()
        new_moves = list(moves)
        new_moves += [func]
        attempt = rec_search(new_cube, new_moves, explored, depth - 1)
        if attempt:
            return attempt

def searchAs(cube):

    moves = []
    explored = []
    border = []
    depth = 0
    return loop_searchAs(cube, moves, explored)



def rec_searchAs(cube, moves, explored, border):

    if cube.check_goal():
        return moves
    if cube.sides in explored:
        return False
    explored += [deepcopy(cube.sides)]
    legal_moves = legal_moves_p(cube)
    for move in legal_moves:
        if move[2].sides not in explored:
            # just to remember: new_node = [heuristic, list of moves/solution, cube state]
            new_node = [move[0] + len(moves) + 1, moves + [move[1]], move[2]]
            border.append(new_node)
    border.sort(key=lambda x: x[0], reverse=True)
    while len(border) > 0:
        heu, new_moves, new_cube = border.pop()
        print(heu)
        attempt = rec_searchAs(new_cube, new_moves, explored, border)
        if attempt:
            return attempt

def loop_searchAs(cube, moves, explored):
    border = [[54, [], cube]]
    while True:
        heu, new_moves, new_cube = border.pop()
        #print(heu)
        if new_cube.check_goal():
            return new_moves
        explored += [deepcopy(new_cube.sides)]
        legal_moves = legal_moves_p(new_cube)
        for move in legal_moves:
            if move[2].sides not in explored:
                # just to remember: new_node = [heuristic, list of moves/solution, cube state]
                new_node = [move[0] + len(new_moves) + 1, new_moves + [move[1]], move[2]]
                border.append(new_node)
        border.sort(key=lambda x: x[0], reverse=True)
        if len(border) > 300:
            border = border[20:]

def heuristic(cube):
    points = 54
    for color in cube.sides:
        for piece in cube.sides[color]:
            if cube.sides[color][piece] == cube.goal_state[color][piece]:
                points -= 1
    return points

def heuristic_2(cube):
    points = 54
    adjacent = {1: (2, 4), 2: (1, 3, 5), 3: (2, 6), 4: (1, 5, 7), 5: (2, 4, 6, 8), 6: (3, 5, 9), 7: (4, 8), 8: (5, 7, 9), 9: (6, 8)}
    for color in cube.sides.values():
        for square in color:
            for adj in adjacent[color[square][1]]:
                if color[square][0] == color[adj][0]:
                    points -= (1 / len(adjacent[color[square][1]]))
    return points

def heuristic_3(cube):
    points = 36
    triples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)]
    for color in cube.sides.values():
        for a, b, c in triples:
            if color[a][0] == color[b][0] == color[c][0]:
                points -= 1
    return points


def legal_moves_p(cube):
    legal_moves = cube.moves()
    list_points = []
    for move in legal_moves:
        new_cube = cube.copy()
        new_cube.moves()[move]()
        list_points += [(heuristic_3(new_cube), move, new_cube)]
    list_points.sort(key=lambda x: x[0], reverse=True)
    return list_points



