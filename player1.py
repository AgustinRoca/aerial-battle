import shapes
import placement

def get_starting_board():
    vehicles = [("BALLOON", 5), ("ZEPPELIN", 2), ("PLANE",3), ("ELEVATOR",1)]
    board = shapes.new_board()
    with open('player_ships.csv') as f:
        for vehicle in vehicles:
            for i in range(vehicle[1]):
                well_placed = False
                while not well_placed:
                    # x,y,z,rotation = input('Enter the coordinates and rotation of your ' + vehicle[0] + ' (x y z rotation): ').split(' ')
                    x, y, z, rotation = f.readline().split(',')
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    rotation = int(rotation)
                    try:
                        place_some_airship(board, x, y, z, rotation, i, vehicle[0])
                        well_placed = True
                    except ValueError:
                        print('Invalid placement, try again')
    return board

def place_some_airship(board, x, y, z, rotation, i, vehicle):
    if vehicle == "BALLOON":
        placement.place_balloon(board, x, y, z, i)
    elif vehicle == "ZEPPELIN":
        placement.place_zeppelin(board, x, y, z, rotation, i)
    elif vehicle == "PLANE":
        placement.place_plane(board, x, y, z, rotation, i)
    elif vehicle == "ELEVATOR":
        placement.place_elevator(board, x, y)

def next_turn(hit_board):
    valid_input = False
    while not valid_input:
        try:
            x, y, z = input('Enter the coordinates to shoot at (x y z): ').split(' ')
            x = int(x)
            y = int(y)
            z = int(z)
            valid_input = True
        except ValueError:
            print('Invalid coordinates, try again')
    return (x, y, z)