import pygame
import random

cacti_sprites = [
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_2.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/big_cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_1.png')
]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()
        self.is_updating = True
        self.image = random.choice(cacti_sprites)
        self.rect = self.image.get_rect(bottomleft=(pos_x, pos_y))
        self.speed = speed

        self.rect.width -= 15

    def update(self):
        if self.is_updating:
            self.rect.x -= self.speed
