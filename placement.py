import shapes

def place_airship(name, board, x_range, y_range, z_range, shape):
    x_start, x_end = x_range
    y_start, y_end = y_range
    z_start, z_end = z_range
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            for z in range(z_start, z_end):
                if shape[x - x_start][y - y_start][z - z_start] == 1:
                    if board[x][y][z] != 'EMPTY':
                        raise ValueError(f'Cannot place airship at ({x}, {y}, {z}) because it overlaps with another airship.')
                    board[x][y][z] = name

def place_balloon(board, x_start, y_start, z_start, balloon_number=0):
    shape = shapes.balloon_shape()
    place_airship(f'BALLOON_{balloon_number}', board, (x_start, x_start + 3), (y_start, y_start + 3), (z_start, z_start + 3), shape)

def place_zeppelin(board, x_start, y_start, z_start, times_rotated=0, zeppelin_number=0):
    shape = shapes.zeppelin_shape()
    x_sum = 5
    y_sum = 2
    for i in range(times_rotated):
        shape = shapes.rotate_shape_anticlockwise(shape)
        x_sum, y_sum = y_sum, x_sum
    place_airship(f'ZEPPELIN_{zeppelin_number}', board, (x_start, x_start + x_sum), (y_start, y_start + y_sum), (z_start, z_start + 2), shape)

def place_plane(board, x_start, y_start, z_start, times_rotated=0, plane_number=0):
    shape = shapes.plane_shape()
    x_sum = 4
    y_sum = 3
    for i in range(times_rotated):
        shape = shapes.rotate_shape_anticlockwise(shape)
        x_sum, y_sum = y_sum, x_sum
    place_airship(f'PLANE_{plane_number}', board, (x_start, x_start + x_sum), (y_start, y_start + y_sum), (z_start, z_start + 2), shape)

def place_elevator(board, x_start, y_start):
    shape = shapes.elevator_shape()
    place_airship('ELEVATOR', board, (x_start, x_start + 1), (y_start, y_start + 1), (0, 10), shape)
