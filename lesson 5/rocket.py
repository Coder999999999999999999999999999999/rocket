import pygame
from pygame.locals import *
from time import *

pygame.init()

screen = pygame.display.set_mode((600,600))

player_x = 200
player_y = 200

keys=[False,False,False,False]

player = pygame.image.load("rocket.png")

backround = pygame.image.load("space.png")

while player_y < 550:
    screen.blit(backround, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #if it is closed the code will stop and the game will be over
            pygame.QUIT()
            exit(0)
        #check keyboard events
        if event.type==KEYDOWN:
            if event.key == K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        #check which key is released
        if event.type==KEYUP:
            #check which key is released
            if event.key == K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False

    #if up arrow is pressed
    if keys[0]==True:
        if player_y > 0:#if player is greater than 0 it is below the top border
            player_y -= 7

    #if down arrow key is pressed 
    if keys[1]==True:
        if player_y < 550:
            player_y += 7

    #if left arrow key is pressed 
    if keys[2]==True:
        if player_x > 0:
            player_x -= 7

    #if right arrow key is pressed 
    if keys[3]==True:
        if player_x > 550:
            player_x += 7

    #by default player should keep moving down
    player_y += 5
    sleep(0.05)

print("Game Over")