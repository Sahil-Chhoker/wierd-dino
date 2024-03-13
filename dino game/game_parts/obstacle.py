import pygame, pymunk
import random

cacti_sprites = [
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_2.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/big_cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_1.png')
]

obstacle_sprite = pygame.Surface((50, 50))
obstacle_sprite.fill("green")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, mass, space):
        super().__init__()
        self.is_updating = True
        self.space = space
        self.mass = mass
        self.image = obstacle_sprite
        self.rect = self.image.get_rect(bottomleft=(pos_x, pos_y))
        self.speed = speed

        self.body = pymunk.Body(self.mass, 100)
        self.body.position = self.rect.center
        self.shape = pymunk.Poly.create_box(self.body, size=self.rect.size)
        self.shape.friction = 1.0
        self.shape.elasticity = 0.0
        self.shape.collision_type = 1  # Set collision_type to 1
        self.space.add(self.body, self.shape)

        self.rect.width -= 15

    def update(self):
        if self.is_updating:
            self.rect.x -= self.speed
            self.body.velocity = -self.rect.x, 0
            self.shape.position = (self.rect.centerx, self.rect.centery)