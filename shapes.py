def new_board():
    board = []
    for x in range(15):
        board.append([])
        for y in range(15):
            board[x].append([])
            for z in range(10):
                board[x][y].append('EMPTY')
    return board

def prismatic_shape(x_len,y_len,z_len):
    shape = []
    for x in range(x_len):
        shape.append([])
        for y in range(y_len):
            shape[x].append([])
            for z in range(z_len):
                shape[x][y].append(1)
    return shape

def balloon_shape():
    return prismatic_shape(3,3,3)

def zeppelin_shape():
    return prismatic_shape(5,2,2)

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
    return prismatic_shape(1,1,10)

def rotate_shape_anticlockwise(shape):
    rotated_shape = []
    for x in range(len(shape[0])):
        rotated_shape.append([])
        for y in range(len(shape)):
            rotated_shape[x].append([])
            for z in range(len(shape[0][0])):
                rotated_shape[x][y].append(shape[y][len(shape[0]) - x - 1][z])

    return rotated_shape
