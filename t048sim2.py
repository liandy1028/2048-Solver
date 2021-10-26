import numpy as np
import random

MOVES = ('up', 'down', 'left', 'right')

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
    best_score = 0
    best_move = 'None'
    for move in MOVES:
        nboard = np.array(board)
        if not make_move(nboard, move):
            continue
        score = simulate_games(nboard)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def simulate_games(board, total_games=100):
    total_score = 0
    for _ in range(total_games):
        nboard = np.array(board)
        while update(nboard):
            while not make_move(nboard, MOVES[random.randint(0,3)]):
                pass
        total_score += score(nboard)
    return total_score / total_games

def update(board):
    zeros = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                zeros.add((i, j))
    for i, j in random.sample(zeros, min(len(zeros), 1)):
        chance = random.randint(0,9)
        if chance != 9:
            board[i][j] = 1
        else:
            board[i][j] = 2

    for move in MOVES:
        tempboard = np.array(board)
        if make_move(tempboard, move):
            return True
    return False

def score(board):
    score = 0
    for row in board:
        for tile in row:
            if tile:
                score += pow(tile, 2) * (tile - 1)
    return score