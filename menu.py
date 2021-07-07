import pygame
from pygame.locals import *
import os
import time
import random

# Initialize sounds
pygame.mixer.init()

# Game Initialization
pygame.init()

# Sounds
pygame.mixer.music.load("menu_song.mp3") 
#wolf_sound = pygame.mixer.Sound(os.path.join('wolf.mp3'))
#sheep_sound = pygame.mixer.Sound(os.path.join('sheep.mp3'))
#button_sound= pygame.mixer.Sound(os.path.join('button.mp3'))

# Play game song
pygame.mixer.Channel(0).play(pygame.mixer.Sound('menu_song.mp3')) 

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
WIDTH = 1020
HEIGHT = 525
screen=pygame.display.set_mode((WIDTH, HEIGHT))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
orange=(254, 157, 78)

# Game Fonts
font = "font_ypy.ttf"
font2 = "font_ys.ttf"
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((WIDTH, HEIGHT )) 

# create a surface object, image is drawn on it. 
wolf_image = pygame.image.load(r'wolf.png')
sheep_image = pygame.image.load(r'sheep.png')

# Main Menu
def main_menu():

    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)

                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)

                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                        pygame.mixer.music.load('button.mp3')
                        pygame.mixer.music.play(0)
                        import main
                        main.main()

                    if selected=="quit":
                        pygame.mixer.music.load('button.mp3')
                        pygame.mixer.music.play(0)
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(black)
        background = pygame.image.load("field.png")
        background = pygame.transform.scale(background, (1020, 525))
        display_surface.blit(background, (0, 0))

        title=text_format("WOLF and SHEEP", font, 75, black)

        # start and quit text
        if selected=="start":
            text_start=text_format("START", font2, 40, black)

        else:
            text_start = text_format("Start", font2, 40, white)

        if selected=="quit":
            text_quit=text_format("QUIT", font2, 30, black)

        else:
            text_quit = text_format("Quit", font2, 30, white )
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Menu image
        display_surface.blit(wolf_image, (0, 3))
        display_surface.blit(sheep_image, (750, 3))
 
        # Main Menu Text
        screen.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Pygame - Tripple Zero")

#Initialize the Game
main_menu()
pygame.quit()
quit()