import agent
import agent2
import gui

def new_hit_board():
    board = []
    for x in range(15):
        board.append([])
        for y in range(15):
            board[x].append([])
            for z in range(10):
                board[x][y].append('?')
    return board

def shoot(board, hit_board, coordinates):
    x, y, z = coordinates
    if hit_board[x][y][z] != '?':
        raise ValueError(f'Cannot shoot at ({x}, {y}, {z}) because it has already been shot at.')
    
    if board[x][y][z] == 'EMPTY':
        hit_board[x][y][z] = 'MISS'
    else:
        airship = board[x][y][z]
        hit_board[x][y][z] = 'HIT'
        print(f'HIT {airship}')
        if count_hits(board, hit_board, airship) >= airship_lives(airship):
            sink_airship(board, hit_board, airship)
        
def airship_lives(airship):
    lives = {
        'BALLOON': 1,
        'ZEPPELIN': 3,
        'PLANE': 2,
        'ELEVATOR': 4,
    }
    return lives[airship.split('_')[0]]
    
def sink_airship(board, hit_board, airship):
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] == airship:
                    hit_board[x][y][z] = 'SUNK'

def count_hits(board, hit_board, airship):
    count = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] == airship and hit_board[x][y][z] == 'HIT':
                    count += 1
    return count

def is_gameover(board, hit_board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] != 'EMPTY' and hit_board[x][y][z] == '?':
                    return False
    return True


def main():
    board1 = agent.get_starting_board()
    board2 = agent2.get_starting_board()

    hit_board_1 = new_hit_board()
    hit_board_2 = new_hit_board()

    i = 0
    while not is_gameover(board1, hit_board_1) and not is_gameover(board2, hit_board_2):
        coordinates1 = agent.next_turn(hit_board_1)
        shoot(board1, hit_board_1, coordinates1)
        coordinates2 = agent2.next_turn(hit_board_2)
        shoot(board2, hit_board_2, coordinates2)
        gui.show_airships_board(board1, hit_board_1, hit_board_2)
        i += 1

    print(i)
    print('Player 1' if is_gameover(board2, hit_board_2) else 'Player 2')

if __name__ == '__main__':
    main()