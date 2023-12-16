import sys, os
import pygame

from pygame.locals import *
from pygame.color import THECOLORS #Dict

pygame.init()

#Display
display = pygame.display.set_mode((600,400))

#To control framerate
clock = pygame.time.Clock() 

display.fill(THECOLORS["white"])

#Variables
framerate = 100
time_s = 0.0
key_e = "U" #Erase
key_f = "U" #Update
user_done = False
mouse_button_UD = "U"

while not user_done:

    dt_s = float(clock.tick(framerate)*1e-3)

    #loop through the list of events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            user_done = True
        elif (event.type ==  pygame.KEYDOWN):
            if (event.key == K_ESCAPE):
                user_done = True
            elif (event.key == K_e):
                key_e = 'D'
            elif (event.key == K_f):
                key_f = 'D'
        elif (event.type ==  pygame.KEYUP):
            if (event.key == K_e):
                key_e = 'U'
            elif (event.key == K_f):
                key_f = 'U'
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_button_UD = 'D'

            # Tuple True/False
            (b1, b2, b3) = pygame.mouse.get_pressed()

            if b1:
                mouse_button = 1
            elif b2:
                mouse_button = 2
            elif b3:
                mouse_button = 3
            else:
                mouse_button = 0
        elif (event.type == pygame.MOUSEBUTTONUP):
            mouse_button_UD = 'U'

    mouse_xy = pygame.mouse.get_pos()

    if ( key_e == 'D'):
        display.fill(THECOLORS["grey"])

    if ((mouse_button_UD == 'D') and (mouse_button == 1)):
        circle_color = THECOLORS["yellow"]
    elif ((mouse_button_UD == 'D') and (mouse_button == 3)):
        circle_color = THECOLORS["red"]
    else:
        circle_color = THECOLORS["blue"]

    pygame.draw.circle(display, circle_color, mouse_xy, 10, 0)

    #Add the incremental time to out time variable
    time_s += dt_s

    print (time_s, dt_s, clock.get_fps())

    if (key_f != 'D'):
        pygame.display.flip()





