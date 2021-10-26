import pygame
import random

class MazeGenorator():
    def __init__(self, Width, Height, Scale):
        self.Scale = Scale
        self.Width = Width
        self.Height = Height
        self.StartCoord = [1, 1]
        self.Spaces = [self.StartCoord]
        self.GenorateAMaze()

    def drawTextMaze(self):
        text = ""
        for h in range(0, self.Height):
            for w in range(0, self.Width):
                if [w, h] in self.Spaces:
                    text += "  "
                else:
                    text += "##"
            text += "\n"
        print(text)

    def MazeDraw(self, screen):
        for Coords in self.Spaces:
            pygame.draw.rect(screen, (255, 255, 255), (Coords[0]*self.Scale, Coords[1]*self.Scale, self.Scale, self.Scale))
        
    def CheckSurroundingSquares(self, Coords):
        PotentialSquares = []
        if [Coords[0]+1, Coords[1]] not in self.Spaces and Coords[0]+1 < self.Height:
            PotentialSquares.append([Coords[0]+1, Coords[1]])
        if [Coords[0]-1, Coords[1]] not in self.Spaces and Coords[0]-1 > -1:
            PotentialSquares.append([Coords[0]-1, Coords[1]])
        if [Coords[0], Coords[1]+1] not in self.Spaces and Coords[1]+1 < self.Width:
            PotentialSquares.append([Coords[0], Coords[1]+1])
        if [Coords[0], Coords[1]-1] not in self.Spaces and Coords[1]-1 > -1:
            PotentialSquares.append([Coords[0], Coords[1]-1])
        
        return PotentialSquares
            

    def GenorateAMaze(self):
        self.CurrentSquare = self.StartCoord
        self.BackTrackIndex = 0

        NotCompleted = True
        while NotCompleted:
            
            self.Potential = self.CheckSurroundingSquares(self.CurrentSquare)
            if len(self.Potential) != 0:
                #check we are not in dead end
                ViableSquares = []
                for square in self.Potential:
                    if len(self.CheckSurroundingSquares(square)) == 3:
                        #ensures no other squares around possible spot are already empty
                        ViableSquares.append(square)
                
                if ViableSquares != []:
                    self.ChosenSquare = random.choice(ViableSquares)
                    self.Spaces.insert(self.BackTrackIndex, self.ChosenSquare)
                else:
                    self.BackTrackIndex += 1
            
            else: #Path has hit a dead end
                self.BackTrackIndex += 1
            
            self.CurrentSquare = self.Spaces[self.BackTrackIndex]
            if self.BackTrackIndex == len(self.Spaces)-1:
                NotCompleted = False

