import pygame

class Player():
    def __init__(self, Scale, Center):
        self.Coords = Center
        self.Scale = Scale
        self.colour = (0, 0, 255)
        self.size = 0.3 * self.Scale

    def ValidMove(self, Spaces):
        self.ShortPotentialCoords = [self.PotentialCoords[0]//self.Scale, self.PotentialCoords[1]//self.Scale]
        if self.Coords != self.PotentialCoords:
            if self.ShortPotentialCoords in Spaces:
                self.Coords = self.PotentialCoords

    def ListenAndMove(self):
        self.PreviousCoords = [self.Coords[0], self.Coords[1]]
        self.PotentialCoords = [self.Coords[0], self.Coords[1]]

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    self.PotentialCoords[0] -= self.Scale
                elif event.key == pygame.K_RIGHT:
                    self.PotentialCoords[0] += self.Scale
                elif event.key == pygame.K_UP:
                    self.PotentialCoords[1] -= self.Scale
                elif event.key == pygame.K_DOWN:
                    self.PotentialCoords[1] += self.Scale

    def Draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.PreviousCoords), self.size)
        pygame.draw.circle(screen, self.colour, (self.Coords), self.size)