import random
import shapes
import placement

def next_turn(hit_board: tuple) -> tuple:
    """Returns the coordinates to shoot next.

    Args:
        hit_board (tuple): A tuple of tuples of tuples of strings representing the hit board. Each cell has 4 possible values: '?', 'HIT', 'MISS', 'SUNK'.

    Returns:
        tuple: (x,y,z) to shoot at.
    """
    
    possible_turns = []
    for x in range(len(hit_board)):
        for y in range(len(hit_board[0])):
            for z in range(len(hit_board[0][0])):
                if hit_board[x][y][z] == '?':
                    possible_turns.append((x, y, z))
    return random.choice(possible_turns)

def get_starting_board():
    """
    Gives the board with the airships placed on it. The board is a 3D array of strings. Each cell has 12 possible values: 'EMPTY', 'BALLOON_0', 'BALLOON_1', 'BALLOON_2', 'BALLOON_3', 'BALLOON_4', 'ZEPPELIN_0', 'ZEPPELIN_1', 'PLANE_0', 'PLANE_1', 'PLANE_2', 'ELEVATOR'.

    Returns:
        tuple: A tuple of tuples of tuples of strings representing the board.
    """
    board = shapes.new_board()
    placement.place_balloon(board, 0, 0, 0, 0)
    placement.place_balloon(board, 10, 0, 7, 1)
    placement.place_balloon(board, 12, 10, 6, 2)
    placement.place_balloon(board, 8, 0, 0, 3)
    placement.place_balloon(board, 0, 8, 0, 4)

    placement.place_zeppelin(board, 0, 0, 4, 0, 0)
    placement.place_zeppelin(board, 8, 10, 8, 1, 1)

    placement.place_plane(board, 7, 7, 1, 0, 0)
    placement.place_plane(board, 5, 0, 6, 1, 1)
    placement.place_plane(board, 1, 10, 6, 2, 2)

    placement.place_elevator(board, 5, 13)
    return board