import pygame as pg
import generate as randomBoard
import solver

WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (251, 234, 235)
LINE_COLOR = (0, 0, 0)
NUM_COLOR = (47, 60, 126)
EDITABLE_NUM_COLOR = (33, 196, 33)
GRID_POS = (75, 75)
CELL_SIZE = 50
BUTTON_COLOR = (200, 200, 200)

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sudoku")

font = pg.font.SysFont("arial", 40)
bold_font = pg.font.SysFont("arial", 40, bold=True)

board = randomBoard.generateBoard()
editable = [[board[i][j] == 0 for j in range(9)] for i in range(9)]

def draw_board(window):
    window.fill(BACKGROUND_COLOR)
    
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pg.draw.line(window, LINE_COLOR, 
                     (GRID_POS[0] + i * CELL_SIZE, GRID_POS[1]), 
                     (GRID_POS[0] + i * CELL_SIZE, GRID_POS[1] + 9 * CELL_SIZE), thickness)
        
        pg.draw.line(window, LINE_COLOR, 
                     (GRID_POS[0], GRID_POS[1] + i * CELL_SIZE), 
                     (GRID_POS[0] + 9 * CELL_SIZE, GRID_POS[1] + i * CELL_SIZE), thickness)

def draw_numbers(window, board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                color = EDITABLE_NUM_COLOR if editable[i][j] else NUM_COLOR
                text = (bold_font if not editable[i][j] else font).render(str(board[i][j]), True, color)
                window.blit(text, (GRID_POS[0] + j * CELL_SIZE + 15, GRID_POS[1] + i * CELL_SIZE + 5))

def draw_buttons(window):
    button_font = pg.font.SysFont("arial", 24, bold=True)
    
    pg.draw.rect(window, BUTTON_COLOR, (75, 540, 100, 40))  
    pg.draw.rect(window, BUTTON_COLOR, (425, 540, 100, 40))  
    
    reset_text = button_font.render("RESET", True, (0, 0, 0))
    solve_text = button_font.render("SOLVE", True, (0, 0, 0))
    
    window.blit(reset_text, (85, 545))
    window.blit(solve_text, (435, 545))

def reset_board():
    global board, editable
    board = randomBoard.generateBoard()
    editable = [[board[i][j] == 0 for j in range(9)] for i in range(9)]

def solve_board():
    global board
    for i in range(9):
        for j in range(9):
            if board[i][j] == "":
                board[i][j] = 0
    solver.SudokuSolver(board)
    editable = [[False for _ in range(9)] for _ in range(9)]

def main():
    running = True
    selected_cell = None

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                
                if GRID_POS[0] < pos[0] < GRID_POS[0] + 9 * CELL_SIZE and GRID_POS[1] < pos[1] < GRID_POS[1] + 9 * CELL_SIZE:
                    x = (pos[0] - GRID_POS[0]) // CELL_SIZE
                    y = (pos[1] - GRID_POS[1]) // CELL_SIZE
                    selected_cell = (y, x)
                
                elif 75 < pos[0] < 175 and 525 < pos[1] < 565:
                    reset_board()
                
                elif 425 < pos[0] < 525 and 525 < pos[1] < 565:
                    solve_board()
            
            if event.type == pg.KEYDOWN and selected_cell:
                if editable[selected_cell[0]][selected_cell[1]]:
                    if event.key in range(pg.K_1, pg.K_9 + 1): 
                        board[selected_cell[0]][selected_cell[1]] = event.key - pg.K_0
                    elif event.key == pg.K_BACKSPACE:
                        board[selected_cell[0]][selected_cell[1]] = 0

        draw_board(window)
        draw_numbers(window, board)
        draw_buttons(window)

        if selected_cell:
            pg.draw.rect(window, (200, 200, 200), 
                         (GRID_POS[0] + selected_cell[1] * CELL_SIZE, 
                          GRID_POS[1] + selected_cell[0] * CELL_SIZE, 
                          CELL_SIZE, CELL_SIZE), 3)

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()
