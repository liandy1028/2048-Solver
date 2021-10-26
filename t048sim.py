import numpy as np
import random

MOVES = ('up', 'down', 'left', 'right')

TRYHARD_MODE = 0

CONST_SCORE = 10
EMPTY_MULTIPLIER = 1
POSSIBLE_MERGES_MULTIPLIER = 1
MONOTONICITY_MULTIPLIER = 2
SUM_MULTIPLIER = 0.2

def make_move(board, move):
    moved = False
    if move == 'left':
        for row in board:
            if shift_row(row):
                moved = True
    elif move == 'up':
        for row in board.T:
            if shift_row(row):
                moved = True
    elif move == 'right':
        for row in np.fliplr(board):
            if shift_row(row):
                moved = True
    elif move == 'down':
        for row in np.flipud(board).T:
            if shift_row(row):
                moved = True
    return moved

def shift_row(row):
    nrow = []
    combo = False
    changed = False
    for i in row:
        if i != 0:
            if combo == True or len(nrow) == 0 or nrow[len(nrow) - 1] != i:
                nrow.append(i)
                combo = False
            else:
                nrow[len(nrow) - 1] += 1
                combo = True
    for i in range(4):
        if i < len(nrow):
            if row[i] != nrow[i]:
                row[i] = nrow[i]
                changed = True
        else:
            row[i] = 0
    return changed

def next_move(board):
    global TRYHARD_MODE
    best_move = 'None'
    best_score = 0
    for move in MOVES:
        score = calculate_score(board, move)
        if score > best_score:
            best_score = score
            best_move = move
    if TRYHARD_MODE == -1:
        for i in range(4):
            for j in range(4):
                if board[i][j] == 10:
                    TRYHARD_MODE = 1
    return best_move

def calculate_score(board, move):
    nboard = np.array(board)
    if not make_move(nboard, move):
        return 0
    return generate_score(nboard)

def generate_score(board, depth=0, depth_limit=3):
    global TRYHARD_MODE
    if depth >= depth_limit:
        return score_board(board)
    total_score = 0
    zeros = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                zeros.add((i, j))
            elif not TRYHARD_MODE and board[i][j] == 10:
                TRYHARD_MODE = -1
            elif TRYHARD_MODE == 1 and board[i][j] == 9:
                TRYHARD_MODE = 2
    if TRYHARD_MODE != 2:
        for i, j in random.sample(zeros, min(len(zeros), 2)):
            nboard2 = np.array(board)
            nboard2[i][j] = 1
            total_score += 0.9 * calculate_move_score(nboard2, depth, depth_limit)

            # nboard4 = np.array(board)
            # nboard4[i][j]
            # total_score += 0.1 * calculate_move_score(nboard4, depth, depth_limit)
    else:
        depth_limit = 4
        for i, j in random.sample(zeros, min(len(zeros), 2)):
            nboard2 = np.array(board)
            nboard2[i][j] = 1
            total_score += 0.9 * calculate_move_score(nboard2, depth, depth_limit)

            # nboard4 = np.array(board)
            # nboard4[i][j]
            # total_score += 0.1 * calculate_move_score(nboard4, depth, depth_limit)
    return total_score

def calculate_move_score(board, depth, depth_limit):
    best_score = 0 
    for move in MOVES:
        nboard = np.array(board)
        if make_move(nboard, move):
            score = generate_score(nboard, depth + 1, depth_limit)
            best_score = max(best_score, score)
    return best_score

def score_board(board):
    score = 0
    
    for row in board:
        for tile in row:
            if tile == 0:
                score += 1

    # for row in board:
    #     score += CONST_SCORE
    #     score += EMPTY_MULTIPLIER * empty_tiles(row)
        # score += POSSIBLE_MERGES_MULTIPLIER * mergeable_tiles(row)
        # score += MONOTONICITY_MULTIPLIER * abs(monotonicity(row))
        # score -= SUM_MULTIPLIER * sum_tiles(row)
    # for col in board.T:
    #     score += CONST_SCORE
    #     score += EMPTY_MULTIPLIER * empty_tiles(col)
    #     # score += POSSIBLE_MERGES_MULTIPLIER * mergeable_tiles(col)
    #     # score += MONOTONICITY_MULTIPLIER * abs(monotonicity(col))
    #     # score -= SUM_MULTIPLIER * sum_tiles(col)
    return score

def empty_tiles(row):
    tiles = 0
    for tile in row:
        if tile == 0:
            tiles += 1
    
    return tiles

def mergeable_tiles(row):
    merges = 0
    previous = 0
    for tile in row:
        if tile != 0:
            if tile == previous:
                merges += 1
                previous = 0
            else:
                previous = tile
    return merges

def monotonicity(row):
    increases = 0
    previous = 0
    for tile in row:
        if tile != 0:
            if tile > previous:
                increases += 1
            elif tile < previous:
                increases -= 1
            previous = tile
    return increases

def sum_tiles(row):
    sum = 0
    for tile in row:
        sum += pow(2, tile)
    return sum


# tboard = np.array([[0,0,2,1],
#                      [0,0,3,5],
#                      [0,0,1,3],
#                      [1,3,1,4]])

# for move in MOVES:
#     n = np.array(tboard)
#     print(make_move(n, move))
#     print(f'{move}, {n}')

# print(next_move(tboard))