import agent1
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

def has_airships_alive(board, hit_board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] != 'EMPTY' and hit_board[x][y][z] == '?':
                    return True
    return False


def main():
    player = 0
    other_player = 1
    agents = [agent1,  agent2]
    boards = [agent1.get_starting_board(), agent2.get_starting_board()]
    hit_boards = [new_hit_board(), new_hit_board()]

    i = 0

    while has_airships_alive(boards[player], hit_boards[other_player]):
        coordinates = agents[player].next_turn(hit_boards[player])
        shoot(boards[other_player], hit_boards[player], coordinates)
        #gui.show_airships_board(boards[player], hit_boards[player], hit_boards[other_player])
        i += 1
        player, other_player = other_player, player

    print(f"Player {other_player} won in {i//2} turns.")

if __name__ == '__main__':
    main()