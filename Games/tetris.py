import random
import curses
from time import sleep

# Inicializar pantalla
screen = curses.initscr()
curses.curs_set(0)

# Definir dimensiones pantalla de juego
s_height, s_width = screen.getmaxyx()
play_height, play_width = 20, 10
play_area_start = [int((s_height - play_height) / 2), int((s_width - play_width) / 2)]

# Definir piezas del tetris
pieces = [
    [
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [0, 2, 2],
        [2, 2, 0],
    ],
    [
        [0, 3, 0],
        [3, 3, 3],
    ],
    [
        [4, 4],
        [4, 4],
    ],
    [
        [0, 5, 0, 0],
        [0, 5, 0, 0],
        [0, 5, 0, 0],
        [0, 5, 0, 0],
    ],
    [
        [0, 6, 6],
        [6, 6, 0],
        [0, 0, 0],
    ],
    [
        [7, 7, 0],
        [0, 7, 7],
        [0, 0, 0],
    ]
]

# Definir colores para las piezas
piece_colors = {
    1: curses.COLOR_CYAN,
    2: curses.COLOR_YELLOW,
    3: curses.COLOR_MAGENTA,
    4: curses.COLOR_BLUE,
    5: curses.COLOR_GREEN,
    6: curses.COLOR_RED,
    7: curses.COLOR_WHITE,
}

def rotate(piece):
    """ Gira la pieza 90 grados en sentido horario """
    new_piece = []
    for i in range(len(piece[0])):
        new_row = []
        for row in piece:
            new_row.append(row[i])
        new_piece.insert(0, new_row)
    return new_piece

def create_board():
    """ Crea una matriz vacía para la pantalla de juego """
    board = []
    for _ in range(play_height):
        new_row = []
        for _ in range(play_width):
            new_row.append(0)
        board.append(new_row)
    return board

def draw_piece(piece, pad, y, x):
    """ Dibuja una pieza en la pantalla de juego """
    color = piece_colors[piece[0][0]]
    for i, row in enumerate(piece):
        for j, val in enumerate(row):
            if val:
                pad.addstr(y+i, x+j*2, '  ', curses.color_pair(color))

def intersects(board, piece, y, x):
    """ Verifica si una pieza se superpone con el tablero ya existente """
    for i, row in enumerate(piece):
        for j, val in enumerate(row):
            if val and board[y+i][x+j]:
                return True
    return False

def main():
    # Asignar colores a las piezas
    for i in range(1, 8):
        curses.init_pair(i, piece_colors[i], curses.COLOR_BLACK)

    # Crear pantalla de juego
    screen.clear()
    curses.start_color()
    curses.init_pair(0, curses.COLOR_WHITE, curses.COLOR_BLACK)
    game_pad = curses.newpad(play_height, play_width*2)
    game_pad.addstr(0, 0, ' '*play_width*2, curses.color_pair(0))
    game_pad.addstr(play_height-1, 0, ' '*play_width*2, curses.color_pair(0))
    for i in range(1, play_height-1):
        game_pad.addstr(i, 0, '  ', curses.color_pair(0))
        game_pad.addstr(i, play_width*2-2, '  ', curses.color_pair(0))
    screen.refresh()

    # Crear tablero del juego
    board = create_board()

    # Iniciar la secuencia de piezas
    current_piece = random.choice(pieces)
    current_color = piece_colors[current_piece[0][0]]
    new_piece = True
    piece_x, piece_y = int(play_width/2 - len(current_piece[0])/2), 0
    score = 0

    while True:
        # Dibujar el juego
        game_pad.clear()
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val:
                    game_pad.addstr(i, j*2, '  ', curses.color_pair(val))
        draw_piece(current_piece, game_pad, piece_y, piece_x*2)
        game_pad.refresh(0, 0, *play_area_start, s_height-1, s_width-1)

        # Esperar por entrada de usuario
        sleep(0.1)
        k = screen.getch()
        if k == curses.KEY_LEFT and not intersects(board, current_piece, piece_y, piece_x-1):
            piece_x -= 1
        elif k == curses.KEY_RIGHT and not intersects(board, current_piece, piece_y, piece_x+1):
            piece_x += 1
        elif k == curses.KEY_DOWN and not intersects(board, current_piece, piece_y+1, piece_x):
            piece_y += 1
        elif k == curses.KEY_UP:
            current_piece = rotate(current_piece)
            if intersects(board, current_piece, piece_y, piece_x):
                current_piece = rotate(current_piece)
                current_piece = rotate(current_piece)
                current_piece = rotate(current_piece)
        elif k == ord('q'):
            break
        
        # Descender la pieza
        if new_piece:
            new_piece = False
            if intersects(board, current_piece, piece_y, piece_x):
                break
        elif not intersects(board, current_piece, piece_y+1, piece_x):
            piece_y += 1
        else:
            # Unir la pieza al tablero
            for i, row in enumerate(current_piece):
                for j, val in enumerate(row):
                    if val:
                        board[piece_y+i][piece_x+j] = current_color

            # Calcular puntuación y eliminar filas completas
            for i, row in enumerate(board):
                if all(row):
                    board.pop(i)
                    new_row = [0 for _ in range(play_width)]
                    board.insert(0, new_row)
                    score += 1
            current_piece = random.choice(pieces)
            current_color = piece_colors[current_piece[0][0]]
            piece_x, piece_y = int(play_width/2 - len(current_piece[0])/2), 0
            new_piece = True

    # Mostrar la puntuación final
    screen.clear()
    msg = "Juego terminado. Puntuación: {}".format(score)
    screen.addstr(int(s_height/2), int((s_width-len(msg))/2), msg)
    screen.refresh()
    sleep(2)

# Iniciar el juego
if __name__ == '_main_':
    curses.wrapper(main)