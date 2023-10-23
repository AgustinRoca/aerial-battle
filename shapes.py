def new_board():
    board = []
    for x in range(15):
        board.append([])
        for y in range(15):
            board[x].append([])
            for z in range(10):
                board[x][y].append('EMPTY')
    return board

def balloon_shape():
    shape = []
    for x in range(3):
        shape.append([])
        for y in range(3):
            shape[x].append([])
            for z in range(3):
                shape[x][y].append(1)
    return shape

def zeppelin_shape():
    shape = []
    for x in range(5):
        shape.append([])
        for y in range(2):
            shape[x].append([])
            for z in range(2):
                shape[x][y].append(1)
    return shape

def plane_shape():
    shape = []
    for x in range(4):
        shape.append([])
        for y in range(3):
            shape[x].append([])
            for z in range(2):
                shape[x][y].append(0)

    for x in range(4):
        shape[x][1][0] = 1

    for y in range(3):
        shape[2][y][0] = 1

    shape[0][1][1] = 1
    
    return shape

def elevator_shape():
    shape = [[[]]]
    for z in range(10):
        shape[0][0].append(1)
    return shape

def rotate_shape_anticlockwise(shape):
    rotated_shape = []
    for x in range(len(shape[0])):
        rotated_shape.append([])
        for y in range(len(shape)):
            rotated_shape[x].append([])
            for z in range(len(shape[0][0])):
                rotated_shape[x][y].append(shape[y][len(shape[0]) - x - 1][z])

    return rotated_shape

def rotate_shape_clockwise(shape):
    rotated_shape = []
    for x in range(len(shape[0])):
        rotated_shape.append([])
        for y in range(len(shape)):
            rotated_shape[x].append([])
            for z in range(len(shape[0][0])):
                rotated_shape[x][y].append(shape[len(shape) - y - 1][x][z])

    return rotated_shape