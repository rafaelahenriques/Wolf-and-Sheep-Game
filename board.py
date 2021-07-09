import pygame


WIDTH, HEIGHT = 500, 500
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
GREEN = (142,185,7)
GREEN_L = (114,159,2)
display_surface = pygame.display.set_mode((WIDTH, HEIGHT )) 

class Board:
    def __init__(self):
        self.board = []
        self.sheep = 1
        self.wolf = 4
    
    def draw_squares(self, win,center):
        win.fill(GREEN)
        background = pygame.image.load("field.png")
        background = pygame.transform.scale(background, (1020, 600))
        display_surface.blit(background, (0, 0))

        for row in range(ROWS):

            for col in range(0,COLS, 2):
                pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREEN_L, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range(col % 2 + 1,COLS, 2):
                pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    