import pygame
import MazeClass as MC
import PlayerClass as PC

pygame.init()
ScreenWidth = 750
ScreenHeight = 750
screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

MazeWidth = 10
MazeLenght = 10
MazeScale = 20
Maze = MC.MazeGenorator(MazeWidth, MazeLenght, MazeScale)

Center = [1.5 * MazeScale, 1.5 * MazeScale]#[int((MazeWidth+1)/2 * MazeScale), int((MazeLenght+1)/2 * MazeScale)]
Player = PC.Player(MazeScale, Center)

MainLoop = True
while MainLoop:

    #QuitPygame on X button hits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainLoop = False
    
    screen.fill([0, 0, 0])
    Maze.MazeDraw(screen)

    CurrentGame = True
    while CurrentGame:
        Player.ListenAndMove()
        Player.ValidMove(Maze.Spaces)
        Player.Draw(screen)
    
        pygame.display.update()
        