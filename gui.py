import numpy as np
import matplotlib.pyplot as plt

def board_to_voxelarray(board, hit_board, colors_dict, hit_colors_dict):
    voxelarray = np.zeros((len(board), len(board[0]), len(board[0][0])), dtype=bool)
    colors = np.empty(voxelarray.shape, dtype=object)
    hit_voxelarray = np.zeros((len(board), len(board[0]), len(board[0][0])), dtype=bool)
    hit_colors = np.empty(hit_voxelarray.shape, dtype=object)
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] != 'EMPTY':
                    if hit_board[x][y][z] == 'HIT':
                        voxelarray[x][y][z] = True
                        colors[x][y][z] = hit_colors_dict[hit_board[x][y][z]]
                    if hit_board[x][y][z] != '?':
                        hit_voxelarray[x][y][z] = True
                        hit_colors[x][y][z] = hit_colors_dict[hit_board[x][y][z]]
                    else:
                        voxelarray[x][y][z] = True
                        colors[x][y][z] = colors_dict[board[x][y][z].split('_')[0]]
    return voxelarray, colors, hit_voxelarray, hit_colors

def hit_board_to_voxelarray(board, colors_dict):
    miss_voxelarray = np.zeros((len(board), len(board[0]), len(board[0][0])), dtype=bool)
    colors = np.empty(miss_voxelarray.shape, dtype=object)
    hit_voxelarray = np.zeros((len(board), len(board[0]), len(board[0][0])), dtype=bool)
    hit_colors = np.empty(hit_voxelarray.shape, dtype=object)
    for x in range(len(board)):
        for y in range(len(board[0])):
            for z in range(len(board[0][0])):
                if board[x][y][z] == 'MISS' or board[x][y][z] == 'SUNK':
                    miss_voxelarray[x][y][z] = True
                    colors[x][y][z] = colors_dict[board[x][y][z]]
                elif board[x][y][z] != '?':
                    hit_voxelarray[x][y][z] = True
                    hit_colors[x][y][z] = colors_dict[board[x][y][z]]

    return miss_voxelarray, colors, hit_voxelarray, hit_colors

def show_airships_board(board, hit_board, hit_board_2, player):
    colors_dict = {
        'BALLOON': 'steelblue',
        'ZEPPELIN': 'lightcoral',
        'PLANE': 'white',
        'ELEVATOR': 'gray',
    }

    hit_colors_dict = {
        'MISS': 'red',
        'HIT': 'green',
        'SUNK': 'black',
    }

    voxelarray, colors, hit_voxelarray, hit_colors = board_to_voxelarray(board, hit_board_2, colors_dict, hit_colors_dict)
    subfigs = plt.figure(figsize=(15,20)).subfigures(1, 2, wspace=0.07)
    ax = subfigs[0].add_subplot(projection='3d')
    ax.voxels(voxelarray, facecolors=colors, alpha=0.8, edgecolors='k', linewidth=0.1)
    ax.voxels(hit_voxelarray, facecolors=hit_colors, edgecolors='gray', linewidth=0.1, alpha=0.1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.title.set_text(f'Player {player} board')

    ax = subfigs[1].add_subplot(projection='3d')
    voxelarray, colors, hit_voxelarray, hit_colors = hit_board_to_voxelarray(hit_board, hit_colors_dict)
    ax.voxels(voxelarray, facecolors=colors, alpha=0.1, edgecolors='k', linewidth=0.1)
    ax.voxels(hit_voxelarray, facecolors=hit_colors, alpha=0.7, edgecolors='k', linewidth=0.1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.title.set_text(f'Player {player} hit board')

    plt.show()
