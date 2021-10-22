from MazeClass import MazeGenorator


import pygame
import MazeClass as MC

pygame.init()
ScreenWidth = 500
ScreenHeight = 500
screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

MazeWidth = 50
MazeLenght = 50
Maze = MC.MazeGenorator(MazeWidth, MazeLenght)

MainLoop = True
while MainLoop:

    #QuitPygame on X button hit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainLoop = False