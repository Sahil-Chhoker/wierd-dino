import pygame

# Constants
HEIGHT = 600
DARK_GREY = (80, 78, 81)

class Ground:
    def __init__(self):
        self.width = 100000
        self.height = 50
        self.rect = pygame.Rect(0, HEIGHT - self.height, self.width, self.height)
        self.ground_color = DARK_GREY

    def draw(self, surface):
        pygame.draw.rect(surface, self.ground_color, self.rect, 4)
