import random

class MazeGenorator():
    def __init__(self, Width, Height):
        #self.Board = [[0 for i in range(Width)] for i in range(Lenght)]
        self.Width = Width
        self.Height = Height
        self.StartCoord = [int(Width/2), int(Height/2)]
        self.Spaces = [self.StartCoord]
        self.GenorateAMaze()
        self.TempMazePrint()

    def TempMazePrint(self):
            printString = ""
            for l in range(0, self.Height):
                for w in range(0, self.Width):
                    if [w, l] in self.Spaces:
                        printString += "  "
                    else:
                        printString += "##"
                printString += "\n"
            print(printString)
        
    def CheckSurroundingSquares(self, Coords):
        PotentialSquares = []
        if [Coords[1]+1, Coords[0]] not in self.Spaces and Coords[1]+1 < self.Height:
            PotentialSquares.append([Coords[1]+1, Coords[0]])
        if [Coords[1]-1, Coords[0]] not in self.Spaces and Coords[1]-1 > -1:
            PotentialSquares.append([Coords[1]-1, Coords[0]])
        if [Coords[1], Coords[0]+1] not in self.Spaces and Coords[0]+1 < self.Width:
            PotentialSquares.append([Coords[1], Coords[0]+1])
        if [Coords[1], Coords[0]-1] not in self.Spaces and Coords[0]-1 > -1:
            PotentialSquares.append([Coords[1], Coords[0]-1])
        
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

