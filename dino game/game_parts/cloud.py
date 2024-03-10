import pygame
import random

cloud_sprite = pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cloud.png')

class Cloud(pygame.sprite.Sprite):
    def __init__(self, posx, posy, speed):
        super().__init__()
        self.is_updating = True
        self.image = cloud_sprite
        self.rect = self.image.get_rect(bottomleft=(posx, posy))
        self.speed = speed

    def update(self):
        if self.is_updating:
            self.rect.x -= self.speed
