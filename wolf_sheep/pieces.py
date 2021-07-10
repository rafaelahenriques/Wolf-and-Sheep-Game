from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

small_wolf = pygame.image.load(r'wolf_samall.png')
small_sheep = pygame.image.load(r'sheep_samall.png')

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, wolf):
        self.row = row
        self.col = col
        self.wolf = wolf
        self.sheep = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        

        if self.wolf == wolf:
            self.direction = -1
        

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_sheep(self):
        self.sheep = True
        
    
   #def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING

        pygame.draw.circle(win, self.wolf, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.sheep, (self.x, self.y), radius)
        if self.sheep:
            win.blit(small_sheep, (self.x - small_sheep.get_width()//2, self.y - small_sheep.get_height()//2))
        if self.wolf:
            win.blit(small_sheep, (self.x - small_wolf.get_width()//2, self.y - small_wolf.get_height()//2))
   
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

 
